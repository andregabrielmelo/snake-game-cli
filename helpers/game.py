from helpers.snake import Snake
from helpers.apple import Apple
import curses

class Game:
    def __init__(self, terminal_height, terminal_width, board_height_start: int, board_height_end: int, board_width_start: int, board_width_end: int, stdscr: curses.window): 
        self.terminal_height: int = terminal_height
        self.terminal_width: int = terminal_width

        self.board_height_start: int = int(board_height_start)
        self.board_height_end: int = int(board_height_end)
        self.board_width_start: int = int(board_width_start)
        self.board_width_end: int = int(board_width_end)

        self.stdscr: curses.window = stdscr
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
                        
    def snake_collision(self):
        """Verify if the snake is in a valid position"""

        if self.snake.head() in [part["position"] for part in self.snake.body[:-1]]:
            self.playing = False

            # Highlight the collision point
            self.stdscr.attron(curses.color_pair(2))  # Enable color (define it in init)
            self.stdscr.addstr(self.snake.head()[1], self.snake.head()[0], "X")  # Mark collision
            self.stdscr.attroff(curses.color_pair(2))  # Disable color
            self.stdscr.refresh()

            curses.napms(500)  # Pause for 500ms to show collision
            
            # Display Game Over message
            self.stdscr.addstr(int(self.terminal_height/2), int(self.terminal_width / 2), "You Lost!", curses.A_UNDERLINE)
            self.stdscr.refresh()

            curses.napms(1500)  # Pause before restart
            return True

                
    def eat_apple(self) -> bool:
        if self.snake.head() == self.apple.position():
            self.score += 1
            self.apple.counter -= 1
            self.apple.generate([body["position"] for body in self.snake.body])
            self.snake.grow()
            return True
        
        return False

    def render(self):
        self.playing = True
        self.stdscr.timeout(10)  # Non-blocking input
        self.stdscr.keypad(True)  # Enable arrow key input
        curses.curs_set(0)  # Hide cursor

        while self.playing:
            self.stdscr.clear()  
            self.display_board()  
            self.display_score()
            self.snake.generate()  
            self.apple.generate([body["position"] for body in self.snake.body])

            key = self.stdscr.getch()  # Get user input
            self.handle_user_input(key) # handle user input
            
            self.snake.move()  # Move the snake
            if (self.snake_collision()):
                 return
            self.eat_apple()

            self.stdscr.refresh()  # Refresh screen
            curses.napms(100)  # Delay to slow down animation

        self.stdscr.nodelay(False)  # Reset blocking input when game stops


