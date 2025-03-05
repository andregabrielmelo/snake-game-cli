from helpers.snake import Snake
from helpers.apple import Apple
import curses

class Game:
    def __init__(self, terminal_height, terminal_width, stdscr): 
        self.terminal_height: int = terminal_height
        self.terminal_width: int = terminal_width
        self.board_height_start: int = 1
        self.board_height_end: int = int(terminal_height)-1
        self.board_width_start: int = 1
        self.board_width_end: int = int(terminal_width*0.8)
        self.stdscr = stdscr
        self.score = 0
        self.snake = Snake(stdscr,  self.board_height_start,  self.board_height_end, self.board_width_start, self.board_width_end)
        self.apple = Apple(stdscr, self.board_height_start,  self.board_height_end, self.board_width_start, self.board_width_end)
    
    def display_board(self):
        """Function that displays the board of the game"""

        for y in range(self.board_height_start, self.board_height_end):
            for x in range(self.board_width_start, self.board_width_end):
                # Fill top left edge
                if y == self.board_height_start and x == self.board_width_start:
                        self.stdscr.addstr(y,x,"┌ ")
                
                # Fill top right edge
                elif y == self.board_height_start and x == self.board_width_end-1:
                        self.stdscr.addstr(y,x,"┐")

                # Fill bottom left edge
                elif y == self.board_height_end-1 and x == self.board_width_start:
                        self.stdscr.addstr(y,x,"└")

                # Fill bottom right edge
                elif y == self.board_height_end-1 and x == self.board_width_end-1:
                        self.stdscr.addstr(y,x,"┘")
                
                # Fill top and bottom
                elif y == self.board_height_start or y == self.board_height_end-1:
                        self.stdscr.addstr(y,x,"─")

                # Fill left and right
                elif x == self.board_width_start or x == self.board_width_end-1:
                    self.stdscr.addstr(y,x,"│")

    def display_score(self):
        self.stdscr.addstr(self.board_height_start,int(self.board_width_end*1.05), f"Score: {self.score}")
        ...

    def handle_user_input(self, key: int) -> bool:
        """Handle movement keys"""
         
        if key == curses.KEY_UP and self.snake.direction != "DOWN":
            self.snake.set_direction("UP")
        elif key == curses.KEY_DOWN and self.snake.direction != "UP":
            self.snake.set_direction("DOWN")
        elif key == curses.KEY_LEFT and self.snake.direction != "RIGHT":
            self.snake.set_direction("LEFT")
        elif key == curses.KEY_RIGHT and self.snake.direction != "LEFT":
            self.snake.set_direction("RIGHT")
        elif key == ord("q"):  # Press 'q' to quit
            self.playing = False
            self.stdscr.clear()
                        
    def valid_position(self):
        """Verify if the snake is in a valid position"""

        for i in range(len(self.snake.body)):
            for j in range(i+1, len(self.snake.body)):
                if self.snake.body[i] == self.snake.body[j]:
                    self.playing = False
                    print("Game over!")
                    return
                
    def eat_apple(self) -> bool:
        if self.snake.head() == self.apple.position():
            self.score += 1
            self.apple.counter -= 1
            self.apple.generate([body["position"] for body in self.snake.body])
            self.snake.grow()
            return True
        
        return False

    def render(self, stdscr):
        self.playing = True
        stdscr.nodelay(True)  # Non-blocking input
        stdscr.keypad(True)  # Enable arrow key input
        curses.curs_set(0)  # Hide cursor

        while self.playing:
            stdscr.clear()  
            self.display_board()  
            self.display_score()
            self.snake.generate()  
            self.apple.generate([body["position"] for body in self.snake.body])

            key = stdscr.getch()  # Get user input
            self.handle_user_input(key) # handle user input
            
            self.eat_apple()
            self.snake.move()  # Move the snake

            stdscr.refresh()  # Refresh screen
            curses.napms(100)  # Delay to slow down animation

        stdscr.nodelay(False)  # Reset blocking input when game stops


