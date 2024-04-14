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
