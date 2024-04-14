import logging
import os

import tomli

logging.basicConfig(level=logging.NOTSET)

SCALE_FACTOR = 2
CONSOLE_WIDTH, CONSOLE_HEIGHT = 80, 25

PALETTE_NAME = "default_ega_16.toml"
colors_config = tomli.load(open(os.path.join("data", "colors", PALETTE_NAME), "rb"))


class ColorPalette:
    BLACK = colors_config["black"]
    BLUE = colors_config["blue"]
    GREEN = colors_config["green"]
    AQUA = colors_config["aqua"]
    RED = colors_config["red"]
    PURPLE = colors_config["purple"]
    YELLOW = colors_config["yellow"]
    WHITE = colors_config["white"]
    GRAY = colors_config["gray"]
    LIGHT_BLUE = colors_config["light_blue"]
    LIGHT_GREEN = colors_config["light_green"]
    LIGHT_AQUA = colors_config["light_aqua"]
    LIGHT_RED = colors_config["light_red"]
    LIGHT_PURPLE = colors_config["light_purple"]
    LIGHT_YELLOW = colors_config["light_yellow"]
    BRIGHT_WHITE = colors_config["bright_white"]


FONT_NAME = "Nouveau_IBM.ttf"
