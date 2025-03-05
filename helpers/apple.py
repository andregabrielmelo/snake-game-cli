import random, curses

class Apple: 
    def __init__(self, stdscr: curses.window, board_height_start: int, board_height_end: int, board_width_start: int, board_width_end: int):
        self.stdscr: curses.window = stdscr
        self.board_height_start: int = int(board_height_start)
        self.board_height_end: int = int(board_height_end)
        self.board_width_start: int = int(board_width_start)
        self.board_width_end: int = int(board_width_end)
        self.x = 0
        self.y = 0
        self.counter: int = 0

    def generate(self) -> bool:
        """Generate a apple randomly in the field"""
        if self.counter > 0:
            self.stdscr.addstr(self.y, self.x, "$")
            return False

        self.x: int = random.randint(self.board_width_start+2, self.board_width_end-2)
        self.y: int = random.randint(self.board_height_start+2, self.board_height_end-2)       
        self.counter += 1

        return True

    def position(self) -> tuple[int, int]:
        return (self.x, self.y)

