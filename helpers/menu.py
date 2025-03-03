import curses

KEY_ENTER = 10

class Menu:
    def __init__(self, height, width):
        self.playing = False
        self.height = height
        self.width = width
        
    def displayMenu(self, stdscr) -> str:
        """Return menu options"""

        options = ["1. Start Game", "2. Instructions", "3. Quit"]

        stdscr.addstr(int(self.height/2-self.height*0.1), int(self.width/2), "SNAKE GAME", curses.A_STANDOUT) # display game title

        for i in range(len(options)):
            stdscr.addstr(int(self.height/2+self.height*i/10), int(self.width/2), options[i])

        return

    def showInstructions(self, stdscr):

        stdscr.addstr(int(self.height/2-self.height*0.1), int(self.width/2), "Eat. Grow. Repeat.", curses.A_BOLD)
        stdscr.addstr(int(self.height/2), int(self.width/2), "Press enter to go the the menu...")
        
        choice = stdscr.getch()
        while(choice != KEY_ENTER):
            stdscr.addstr(int(self.height*0.9), int(self.width/2), "Press enter?", curses.A_UNDERLINE)
            choice = stdscr.getch()
        else:
            return
