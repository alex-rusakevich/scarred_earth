from typing import List

from pygame import Surface

from scripts.font import *
from scripts.settings import ColorPalette


class Cell:
    value: str = ""
    bg: str = ""
    fg: str = ""

    def __init__(self, value="@", bg=ColorPalette.BLACK, fg=ColorPalette.WHITE) -> None:
        self.value = value
        self.bg = bg
        self.fg = fg

    def render(self) -> Surface:
        return DEFAULT_FONT.render(self.value, True, self.fg, self.bg)


class Console:
    carriage_pos = 1, 1
    matrix: List[List[Cell]]
    redraw_pending = True

    def __init__(self) -> None:
        self.matrix = (
            (Cell() for _ in range(CONSOLE_WIDTH)) for _ in range(CONSOLE_HEIGHT)
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

        def wrapped(self: Console):
            self.redraw_pending = True

            return fn(self)

        return wrapped

    def set_pos(self, x, y):
        self.carriage_pos = x, y

    # def print(text: str, )
