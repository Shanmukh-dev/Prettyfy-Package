import platform

from .Decor import Decor
from .Win7_Colorizer import Win7_Colorizer
from .ANSI_Colorizer import ANSI_Colorizer
from .MenuDriver import MenuDriver


TextColorizer = Win7_Colorizer if "Windows" in platform.platform() and int(platform.release()) < 10 else ANSI_Colorizer


def colorizeText(string = "", FgColor : str = None, BgColor : str = None, JustTextBG: bool = False):

    only_text = JustTextBG

    TextColorizer(string = string, FgColor = FgColor, BgColor = BgColor).Colorize(JustTextBG = only_text)
