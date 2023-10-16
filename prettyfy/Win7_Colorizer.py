import ctypes as ct
from .ColorSet import ColorSet

import os


class Win7_Colorizer():
    # ct.windll.kernel32.SetConsoleTextAttribute(stdout,0x0080 | 0x0008 |0x0070 | 0x0004)
    # bgIntensity|fgIntensity|BgColor|FgColor
    DefaultFg: str = "WHITE"
    DefaultBg: str = "BLACK"
    intensify: bool = False
    def Print(text : str = None, sep: str = " ", end: str = "\n"):
        width = os.get_terminal_size().columns 
        text = " " if text == "" else text
        
        if text != None:
            text = str(text)
            lines = text.splitlines()
            length = [(len(line), line) for line in lines]
            for line in length:
                
                print(line[1] + " " * (width - line[0]), sep=sep, end=end)

    def __init__(self, string="", FgColor: str = None, BgColor: str = None) -> None:

        FgColor = self.DefaultFg if FgColor == None else FgColor
        BgColor = self.DefaultBg if BgColor == None else BgColor

        self.STDHANDLE = -11

        self.COLORS = ColorSet.WIN7_COLOR_SET
        self.stdout = ct.windll.kernel32.GetStdHandle(self.STDHANDLE)
        self.colorInitiator = ct.windll.kernel32.SetConsoleTextAttribute

        self.default_fg = self.COLORS["FOREGROUND"][self.DefaultFg]
        self.default_bg = self.COLORS["BACKGROUND"][self.DefaultBg]

        self.BgColor = BgColor
        self.FgColor = FgColor
        self.string = string

        # self.SetDefaultTheme()

    def CPrint(self, text : str = None, JustTextBG : bool= False):
        width = os.get_terminal_size().columns 
        if text != None:
            text = str(text)

            lines = text.splitlines()
            max_len =  max([len(line) for line in lines])
            length_lines = [(len(line), line) for line in lines]
            for i, line in enumerate(length_lines):
                if not JustTextBG:
                    # print(JustTextBG)

                    print(line[1] + " " * (width - line[0]))
                else:

                    print(line[1])

    def colorInitiation(self):
        if self.intensify:
            self.colorInitiator(
                self.stdout, self.COLORS["BACKGROUND"]["INTENSITY"] | self.COLORS["FOREGROUND"]["INTENSITY"] | self.COLORS["BACKGROUND"][self.BgColor] | self.COLORS["FOREGROUND"][self.FgColor])

           

        else:
            self.colorInitiator(
                self.stdout, self.COLORS["BACKGROUND"][self.BgColor] | self.COLORS["FOREGROUND"][self.FgColor])

            

    def Colorize(self, JustTextBG : bool = False):
        if self.intensify:
            self.colorInitiator(
                self.stdout, self.COLORS["BACKGROUND"]["INTENSITY"] | self.COLORS["FOREGROUND"]["INTENSITY"] | self.COLORS["BACKGROUND"][self.BgColor] | self.COLORS["FOREGROUND"][self.FgColor])
            
            onlyText = JustTextBG
            
            self.CPrint(self.string, JustTextBG = onlyText)

            self.colorInitiator(self.stdout, self.COLORS["BACKGROUND"]["INTENSITY"] | self.COLORS["FOREGROUND"]["INTENSITY"] | self.default_bg | self.default_fg)

        else:
            self.colorInitiator(
                self.stdout, self.COLORS["BACKGROUND"][self.BgColor] | self.COLORS["FOREGROUND"][self.FgColor])
            onlyText = JustTextBG
            
            
            self.CPrint(self.string, JustTextBG = onlyText)
            # self.CPrint(self.string)

            self.colorInitiator(self.stdout, self.default_bg | self.default_fg)

    def SetDefaultTheme(self):
        if self.intensify:
            self.colorInitiator(self.stdout, self.COLORS["BACKGROUND"]["INTENSITY"] |
                                self.COLORS["FOREGROUND"]["INTENSITY"] | self.default_bg | self.default_fg)
        else:
            self.colorInitiator(self.stdout, self.default_bg | self.default_fg)

    def Reset(self):
        self.colorInitiator(
            self.stdout, self.COLORS["BACKGROUND"]["BLACK"] | self.COLORS["FOREGROUND"]["WHITE"])


# -----------------------------------Tests---------------------------------------------------- #


# Win7_Colorizer(string="Hope this works", DefaultBg="RED",
#             DefaultFg="BLUE").Colorize()
# print("")
# Win7_Colorizer(FgColor="BLACK", BgColor="CYAN", string="Hope this works",
#             DefaultBg="RED", DefaultFg="BLUE").Colorize()
# print("")

# Win7_Colorizer(string="Hope this works", DefaultBg="RED",
#             DefaultFg="BLUE").Colorize()

# Win7_Colorizer().Reset()


# colorize = Win7_Colorizer

# colorize.DefaultBg = "CYAN"
# colorize.DefaultFg = "BLACK"

# colorize().SetDefaultTheme()
# colorize(FgColor="BLACK", BgColor="CYAN", string="Hope this works...").Colorize()

# colorize.intensify = True

# colorize(FgColor="WHITE", BgColor="RED", string="This must be bright").Colorize()

# colorize.intensify = False

# colorize(FgColor="WHITE", BgColor="RED", string="This must be normal").Colorize()


# colorize().Reset()
