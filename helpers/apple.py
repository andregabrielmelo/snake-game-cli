import random, curses

class Apple: 
    def __init__(self, board_height, board_width, stdscr):
        self.stdscr: curses.window = stdscr
        self.board_height: int = board_height
        self.board_width: int = board_width
        self.counter: int = 0

    def create_apple(self) -> tuple:
        """Generate a apple randomly in the field"""

        # Pick random x point
        x: int = random.randint(int(self.board_width*0.25)+2, int(self.board_width*0.75)-2)

        # Pick random y
        y: int = random.randint(int(self.board_height*0.25)+2,int(self.board_height*0.75)-2)

        return (x, y)
    
    def display_apple(self, x, y) -> bool:
        self.stdscr.addstr(y, x, "$")
        return True


