import os
from logging import getLogger

import pygame

from scripts.settings import *

logger = getLogger(__name__)

pygame.font.init()
DEFAULT_FONT = pygame.font.Font(
    os.path.join("data", "fonts", FONT_NAME), 14 * SCALE_FACTOR
)
CHAR_WIDTH, CHAR_HEIGHT = DEFAULT_FONT.size("W")

logger.info(f"Character size: {CHAR_WIDTH}x{CHAR_HEIGHT}")
