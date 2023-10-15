import curses
from curses import wrapper
import time


class MenuDriver:
    def __init__(self, MenuList) -> None:
        
        # self.screen = curses.initscr()
        self.MenuList = MenuList
        self.choice = 0

        wrapper(self.Menu)


    def Menu(self, stdscr):
       
        self.stdscr = stdscr
        self.heigth, self.width = self.stdscr.getmaxyx()

        self.winWidth = max([len(i) for i in self.MenuList])
        self.winheight = len(self.MenuList)

        self.x = (self.width - self.winWidth) // 2
        self.y = (self.heigth - self.winheight) // 2
        self.stdscr.clear()
        while True:
            
            self.stdscr.clear()
            for i, option in enumerate(self.MenuList):
                if i == self.choice:
                    self.stdscr.addstr(f">> {option}\n", curses.A_REVERSE)
                    self.stdscr.refresh()
                else:
                    self.stdscr.addstr(f"{option}\n")
                    self.stdscr.refresh()
            # self.screen.keypad(True)
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
                self.stdscr.addstr(f"Redirecting to {self.MenuList[self.choice]}")
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