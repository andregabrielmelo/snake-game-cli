import curses

KEY_ENTER = 10

class Menu:
    def __init__(self, terminal_height, terminal_width, stdscr):
        self.playing = False
        self.terminal_height = terminal_height
        self.terminal_width = terminal_width
        self.stdscr = stdscr
        
    def displayMenu(self) -> None:
        """Show menu items"""

        menu_items: list[dict] = [
            {
                "display": "SNAKE GAME",
                "option": curses.A_STANDOUT, 
            },
            {
                "display": "1. Start Game",
                "option": curses.A_NORMAL,
            }, 
            {
                "display": "2. Instructions",
                "option": curses.A_NORMAL,
            }, 
            {
                "display": "3. Quit",
                "option": curses.A_NORMAL,
            },
        ]

        # display menu itmes
        for i in range(len(menu_items)):
            self.stdscr.addstr(int(self.terminal_height/2+self.terminal_height*i/10), int(self.terminal_width/2), menu_items[i]["display"], menu_items[i]["option"])

    def showInstructions(self, stdscr) -> None:
        """Show instructions items"""

        instruction_items: list[dict] = [
            {
                "display": "Eat. Grow. Repeat.",
                "option": curses.A_BOLD, 
            },
            {
                "display": "Press enter to go the the menu...",
                "option": curses.A_NORMAL,
            }, 
        ]

        for i in range(len(instruction_items)):
            self.stdscr.addstr(int(self.terminal_height/2+self.terminal_height*i/10), int(self.terminal_width/2), instruction_items[i]["display"], instruction_items[i]["option"])
        
        choice = stdscr.getch()
        while(choice != KEY_ENTER):
            stdscr.addstr(int(self.terminal_height*0.9), int(self.terminal_width/2), "Press enter?", curses.A_UNDERLINE)
            choice = stdscr.getch()
