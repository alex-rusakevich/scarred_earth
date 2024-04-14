import logging
from typing import List

from pygame import Surface

from scripts.font import *
from scripts.settings import ColorPalette

logger = logging.getLogger(__name__)


class Cell:
    value: str = ""
    bg: str = ""
    fg: str = ""

    def __init__(self, value=" ", bg=ColorPalette.BLACK, fg=ColorPalette.WHITE) -> None:
        self.value = value
        self.bg = bg
        self.fg = fg

    def render(self) -> Surface:
        return DEFAULT_FONT.render(self.value, FONT_ANTIALIASING, self.fg, self.bg)


class Console:
    carriage_pos = 1, 1
    matrix: List[List[Cell]]
    redraw_pending = True

    def __init__(self) -> None:
        self.matrix = list(
            tuple(Cell() for x in range(CONSOLE_WIDTH)) for y in range(CONSOLE_HEIGHT)
        )

    def render(self) -> Surface:
        """Prepare surface for drawing

        :return: surface ready to blit
        :rtype: Surface
        """
        surface = Surface((80 * CHAR_WIDTH, 25 * CHAR_HEIGHT))

        for row_number, row in enumerate(self.matrix):
            for cell_number, cell in enumerate(row):
                surface.blit(
                    cell.render(),
                    (cell_number * CHAR_WIDTH, row_number * CHAR_HEIGHT),
                )

        return surface

    def draw(self) -> None:
        """if redraw_pending is set, then render a console surface and apply to screen, skip drawing otherwise

        :rtype: None
        """
        if self.redraw_pending:
            self.redraw_pending = False
            pygame.display.get_surface().blit(self.render(), (0, 0))

    def causes_redraw(fn):
        """Wrapper for functions which lead to console redraw

        :param fn: wrapped function
        :type fn: function
        """

        def wrapped(self, *args, **kwargs):
            self.redraw_pending = True

            return fn(self, *args, **kwargs)

        return wrapped

    @causes_redraw
    def shift_matrix_up(self):
        self.matrix.pop(0)
        self.matrix.append(tuple(Cell() for _ in range(CONSOLE_WIDTH)))

    @causes_redraw
    def set_pos(self, x, y):
        self.carriage_pos = x, y

    @causes_redraw
    def print(
        self,
        value: str,
        bg=ColorPalette.BLACK,
        fg=ColorPalette.WHITE,
        carriage_pos: tuple = None,
    ):
        """Print text to console

        :param value: text to print
        :type value: str
        :param bg: background color, defaults to ColorPalette.BLACK
        :type bg: str, optional
        :param fg: foreground text color, defaults to ColorPalette.WHITE
        :type fg: str, optional
        :param carriage_pos: text position in console, `(x, y)`, both start with 1, defaults to self.carriage_pos
        :type carriage_pos: tuple, optional
        """

        if not carriage_pos:
            carriage_pos = self.carriage_pos

        cx, cy = carriage_pos
        cx -= 1
        cy -= 1

        for ch in value:
            # logger.debug(f"setting character at X:{cx}, Y:{cy}")

            if ch == "\n":  # Move to next line if next line character encountered
                cy += 1
                cx = 0
                continue

            # region Set cell
            cell = self.matrix[cy][cx]
            cell.value = ch
            cell.bg = bg
            cell.fg = fg
            # endregion

            if (
                cy + 1 == CONSOLE_HEIGHT and cx + 1 == CONSOLE_WIDTH
            ):  # Last character of last row
                self.shift_matrix_up()
                cx = 0
            elif cx + 1 == CONSOLE_WIDTH:  # Last cell in row
                cx = 0
                cy += 1
            else:  # Cell inside row
                cx += 1

        self.carriage_pos = (cx + 1, cy + 1)

    @causes_redraw
    def println(self, value: str, *args, **kwargs):
        """Print the text and move to new line. See `print` function for info

        :param value: the text to be printed
        :type value: str
        """
        self.print(value + "\n", *args, **kwargs)
