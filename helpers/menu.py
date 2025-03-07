import curses
from helpers.functions import prompt_user

KEY_ENTER = 10

class Menu:
    def __init__(self, terminal_height, terminal_width, board_height_start: int, board_height_end: int, board_width_start: int, board_width_end: int, stdscr):
        self.stdscr = stdscr

        self.board_height_start: int = int(board_height_start)
        self.board_height_end: int = int(board_height_end)
        self.board_width_start: int = int(board_width_start)
        self.board_width_end: int = int(board_width_end)

        self.terminal_height = terminal_height
        self.terminal_width = terminal_width
        
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
            self.stdscr.addstr(int(self.terminal_height*0.2+self.terminal_height*i/10), int(self.board_width_end*1.05), menu_items[i]["display"], menu_items[i]["option"])

    def showInstructions(self) -> None:
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
        
        prompt_user(self.stdscr, int(self.terminal_height*0.8), int(self.terminal_width/2), "Press enter?", KEY_ENTER)