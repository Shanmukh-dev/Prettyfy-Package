from .ColorSet import ColorSet

import os
import sys


class ANSI_Colorizer:
    DefaultFg : str = "WHITE"
    DefaultBg : str = "BLACK"

    def Print(text = None, sep: str = " ", end: str = "\n"):
        width = os.get_terminal_size().columns 
        text = " " if text == "" else text
        if text != None:
            text = str(text)
            lines = text.splitlines()
            length = [(len(line), line) for line in lines]
            for line in length:
                # print(line[0])
                # print(line[1] + self.DefaultColorEscape, end="\r")
                print(line[1] + " " * (width - line[0]), sep = sep, end = end)


    def __init__(self, string = "", FgColor : str = None, BgColor : str = None) -> None:
        if sys.platform == 'win32': os.system("")

        self.COLORS = ColorSet.REGULAR_COLOR_SET

        FgColor = self.DefaultFg if FgColor == None else FgColor
        BgColor = self.DefaultBg if BgColor == None else BgColor


        self.default_fg = self.COLORS["FOREGROUND"][self.DefaultFg]
        self.default_bg = self.COLORS["BACKGROUND"][self.DefaultBg]

        self.FgColor = self.COLORS["FOREGROUND"][FgColor]
        self.BgColor = self.COLORS["BACKGROUND"][BgColor]
        self.string = string

        self.ColorEscape = f"\x1b[{self.FgColor};{self.BgColor}m"
        self.DefaultColorEscape = f"\x1b[{self.default_fg};{self.default_bg}m"
        self.ResetEscape = "\x1b[37;40m"

    def CPrint(self, text: str = None, JustTextBG : bool | None = False):
        width = os.get_terminal_size().columns 

        if text != None:
            text = str(text)

            lines = text.splitlines()
            
            length_lines = [(len(line), line) for line in lines]

            
            for i, line in enumerate(length_lines):
                if not JustTextBG:
                    print(line[1] + " " * (width - line[0]), end="")
                else:
                    print(line[1] , end="")
                    print(self.DefaultColorEscape, end="")
                    if i == len(length_lines) - 1:
                        print(" " * (width - line[0]), end= "")
                        print(self.DefaultColorEscape, end="")

                    else:
    
                        print(" " * (width - line[0]))
                        print(self.ColorEscape, end="")

    def Colorize(self, JustTextBG : bool = False):
        print(self.ColorEscape, end="")

        text = self.string
        self.CPrint(text = str(text), JustTextBG = JustTextBG)

        print(self.DefaultColorEscape, end="\n")

    # def Colorize(self):
    #     print(self.ColorEscape + self.string + self.DefaultColorEscape)

    def Reset(self):
        print(self.ResetEscape)

    def SetDefaultTheme(self):
        print(self.DefaultColorEscape + "")



# -----------------------------------Tests---------------------------------------------------- #


# colorize = ANSI_Colorizer


# colorize.DefaultBg = "BRIGHT_CYAN"
# colorize.DefaultFg = "BLACK"

# colorize().SetDefaultTheme()

# colorize(FgColor="BLACK", BgColor="BRIGHT_CYAN", string="Hope this works...").Colorize()

# colorize().Reset()
