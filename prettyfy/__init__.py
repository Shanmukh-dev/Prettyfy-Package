import platform

from .Decor import Decor
from .Win7_Colorizer import Win7_Colorizer
from .ANSI_Colorizer import ANSI_Colorizer
from .MenuDriver import MenuDriver


TextColorizer = Win7_Colorizer
# TextColorizer = Win7_Colorizer if "Windows" in platform.platform() and int(platform.release()) < 10 else ANSI_Colorizer