from .ColorSet import ColorSet
from .Decor import Decor

import curses
from curses import wrapper
import time


class MenuDriver:
    def __init__(self, TextColorizer, MenuList, FgColor : str = None, BgColor : str = None, header: str = " ", header_border_style = "simple", separatorStyle = "simple_dash") -> None:
        
        self.MenuList = MenuList
        self.choice = 0

        self.colors = ColorSet.MENU_COLOR_SET#

        self.header = "---Menu header here---" if header == " " else header
        self.header_border_style = header_border_style
        self.separatorStyle = separatorStyle

        self.colors = ColorSet.MENU_COLOR_SET#

        self.default_fg = self.colors[TextColorizer.DefaultFg]#
        self.default_bg = self.colors[TextColorizer.DefaultBg]#

        self.FgColor = self.colors[TextColorizer.DefaultFg] if FgColor == None else FgColor#
        self.BgColor = self.colors[TextColorizer.DefaultBg] if FgColor == None else BgColor#

        wrapper(self.Menu)


    def Menu(self, stdscr):
       
        self.stdscr = stdscr

        self.maxWidth = max([len(i) for i in self.MenuList])
        curses.init_pair(1, self.FgColor, self.BgColor)


        
        self.stdscr.clear()
        
        

        while True:
            
            self.stdscr.clear()

            self.stdscr.addstr(f"{Decor.boxstr(style = self.header_border_style, string = self.header)}\n\n", curses.color_pair(1))

            self.stdscr.addstr("+", curses.color_pair(1))
            self.stdscr.addstr(Decor.drawLine(style = self.separatorStyle, length = self.maxWidth + 2), curses.color_pair(1))
            self.stdscr.addstr("+\n", curses.color_pair(1))

            for i, option in enumerate(self.MenuList):
                if i == self.choice:
                    self.stdscr.addstr(f">> {option}\n", curses.color_pair(1) | curses.A_REVERSE| curses.A_BOLD | curses.A_BLINK)
                    self.stdscr.refresh()
                else:
                    self.stdscr.addstr(f"{option}\n", curses.color_pair(1))
                    self.stdscr.refresh()

            self.stdscr.addstr("+", curses.color_pair(1))
            self.stdscr.addstr(Decor.drawLine(style = self.separatorStyle, length = self.maxWidth + 2), curses.color_pair(1))
            self.stdscr.addstr("+\n", curses.color_pair(1))
            self.stdscr.addstr("\n# Use arrow keys to navigate\n# Press Enter to select\n# Press Esc to cancell\n\n", curses.color_pair(1))#

            try:
                self.key = self.stdscr.getkey()
            except:
                self.key = None
            
            
            if self.key == "KEY_RIGHT" or self.key == "KEY_DOWN":
                if self.choice >= len(self.MenuList) - 1:
                    self.choice = 0
                else:
                    self.choice += 1
            elif self.key == "KEY_LEFT" or self.key == "KEY_UP":
                if self.choice <= 0:
                    self.choice = len(self.MenuList) - 1
                else:
                    self.choice -= 1
            elif self.key == "\n":
                self.stdscr.addstr(f"Redirecting to {self.MenuList[self.choice]}", curses.color_pair(1) | curses.A_REVERSE| curses.A_BOLD | curses.A_BLINK)
                self.stdscr.refresh()

                time.sleep(1.5)
                break
            elif self.key == "\x1b":
                self.stdscr.addstr("Cancelled. Press any key to continue.")
                self.stdscr.refresh()

                self.stdscr.getch()
                break

    def GetChoice(self):
        return self.MenuList[self.choice]
           



# choice = MenuDriver(MenuList = ["Option1", "Option2", "Option3", "Option4"]).GetChoice()

# print(choice)