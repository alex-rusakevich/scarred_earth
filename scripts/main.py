from logging import getLogger

import pygame
import pygame.font
import pygame.time

from scripts.console import Console
from scripts.font import *
from scripts.settings import *

logger = getLogger(__name__)


def run_game():
    pygame.init()

    screen_width, screen_height = (
        CONSOLE_WIDTH * CHAR_WIDTH,
        CONSOLE_HEIGHT * CHAR_HEIGHT,
    )
    logger.info(f"Screen size: {screen_width}x{screen_height}")

    pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    pygame.display.update()

    console = Console()
    console.println(
        """1. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Diam ut venenatis tellus in metus. Sit amet luctus venenatis lectus magna. Scelerisque in dictum non consectetur. Lacus luctus accumsan tortor posuere ac ut consequat. Odio pellentesque diam volutpat commodo sed egestas egestas. Porttitor rhoncus dolor purus non enim. Consequat semper viverra nam libero justo laoreet sit amet. Posuere morbi leo urna molestie at. Eu feugiat pretium nibh ipsum consequat nisl. Nulla pellentesque dignissim enim sit amet venenatis urna. Velit dignissim sodales ut eu sem integer. Phasellus faucibus scelerisque eleifend donec pretium vulputate sapien nec sagittis."""
    )
    console.println(
        """2. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Diam ut venenatis tellus in metus. Sit amet luctus venenatis lectus magna. Scelerisque in dictum non consectetur. Lacus luctus accumsan tortor posuere ac ut consequat. Odio pellentesque diam volutpat commodo sed egestas egestas. Porttitor rhoncus dolor purus non enim. Consequat semper viverra nam libero justo laoreet sit amet. Posuere morbi leo urna molestie at. Eu feugiat pretium nibh ipsum consequat nisl. Nulla pellentesque dignissim enim sit amet venenatis urna. Velit dignissim sodales ut eu sem integer. Phasellus faucibus scelerisque eleifend donec pretium vulputate sapien nec sagittis."""
    )
    console.println(
        """3. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Diam ut venenatis tellus in metus. Sit amet luctus venenatis lectus magna. Scelerisque in dictum non consectetur. Lacus luctus accumsan tortor posuere ac ut consequat. Odio pellentesque diam volutpat commodo sed egestas egestas. Porttitor rhoncus dolor purus non enim. Consequat semper viverra nam libero justo laoreet sit amet. Posuere morbi leo urna molestie at. Eu feugiat pretium nibh ipsum consequat nisl. Nulla pellentesque dignissim enim sit amet venenatis urna. Velit dignissim sodales ut eu sem integer. Phasellus faucibus scelerisque eleifend donec pretium vulputate sapien nec sagittis."""
    )

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        console.draw()
        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    quit()
