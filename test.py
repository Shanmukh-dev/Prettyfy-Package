import prettyfy
from prettyfy import *

def Option1():
    print("This is option 1")
def Option2():
    print("This is option 2")
def Option3():
    print("This is option 3")
def Option4():
    print("This is option 3")


menuList = ["Option1", "Option2", "Option3", "Option4"]

choice = MenuDriver(MenuList=menuList).GetChoice()

exec(f"{choice}()")








colorize = TextColorizer



colorize.DefaultBg = "CYAN"
colorize.DefaultFg = "BLACK"

colorize().SetDefaultTheme()
colorize(FgColor="BLACK", BgColor="CYAN", string="Hope this works...").Colorize()

colorize.intensify = True

colorize(FgColor="WHITE", BgColor="RED", string="This must be bright").Colorize()


colorize.intensify = False

colorize(FgColor="WHITE", BgColor="RED", string="This must be normal").Colorize()


colorize().Reset()


