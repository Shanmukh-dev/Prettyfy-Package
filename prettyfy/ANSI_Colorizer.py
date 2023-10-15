from .ColorSet import ColorSet


class ANSI_Colorizer:
    DefaultFg : str = "WHITE"
    DefaultBg : str = "BLACK"

    def __init__(self, string = "", FgColor : str = None, BgColor : str = None) -> None:

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

        
    def colorInitiation(self):
        print(self.ColorEscape)

    def Colorize(self):
        print(self.ColorEscape + self.string + self.DefaultColorEscape)

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
