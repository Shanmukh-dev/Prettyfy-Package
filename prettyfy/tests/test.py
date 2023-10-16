import prettyfy
from prettyfy import *
# from prettyfy.TextColorizer() import Print


# def Option1():
#     print("This is option 1")
# def Option2():
#     print("This is option 2")
# def Option3():
#     print("This is option 3")
# def Option4():
#     print("This is option 3")


# menuList = ["Option1", "Option2", "Option3", "Option4"]

# choice = MenuDriver(MenuList=menuList).GetChoice()

# exec(f"{choice}()")



colorize = TextColorizer

Print = colorize.Print


colorize.DefaultBg = "CYAN"
colorize.DefaultFg = "BLACK"

colorize().SetDefaultTheme()
colorize(FgColor="BLACK", BgColor="CYAN", string="Hope this works...").Colorize()

colorize.intensify = True

# colorize(FgColor="BRIGHT_WHITE", BgColor="BRIGHT_RED", string="This must be bright").Colorize()
colorize(FgColor="WHITE", BgColor="RED", string="This must be bright").Colorize()


colorize.intensify = False


colorize(FgColor="WHITE", BgColor="RED", string="This must be normal JustTextBG").Colorize(JustTextBG = True)


colorize(FgColor="WHITE", BgColor="RED", string="""This must be normal
...I think""").Colorize()

Print(text="This is another print")


colorize(FgColor="WHITE", BgColor="RED", string="""This must be normal
...I think JustTextBG""").Colorize(JustTextBG = True)


Print(text=45654)
Print(text="This is another print")
Print(text="This is another print")


input()


colorize().Reset()


