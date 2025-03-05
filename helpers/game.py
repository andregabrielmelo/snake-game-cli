from helpers.snake import Snake
from helpers.apple import Apple
import os, random, datetime, curses

class Game:
    def __init__(self, height, width, stdscr): 
        self.terminal_height: int = height
        self.terminal_width: int = width
        self.stdscr = stdscr
        self.score = 0
        self.snake = Snake(height, width, stdscr)
        self.apple = Apple(height, width, stdscr)
    
    def display_board(self, stdscr):
        """Function that displays the board of the game"""

        for y in range(int(self.terminal_height*0.25), int(self.terminal_height*0.75)):
            for x in range(int(self.terminal_width*0.25), int(self.terminal_width*0.75)):
                # Fill top left edge
                if y == int(self.terminal_height*0.25) and x == int(self.terminal_width*0.25):
                        stdscr.addstr(y,x,"┌ ")
                
                # Fill top right edge
                elif y == int(self.terminal_height*0.25) and x == int(self.terminal_width*0.75)-1:
                        stdscr.addstr(y,x,"┐")

                # Fill bottom left edge
                elif y == int(self.terminal_height*0.75)-1 and x == int(self.terminal_width*0.25):
                        stdscr.addstr(y,x,"└")

                # Fill bottom right edge
                elif y == int(self.terminal_height*0.75)-1 and x == int(self.terminal_width*0.75)-1:
                        stdscr.addstr(y,x,"┘")
                
                # Fill top and bottom
                elif y == int(self.terminal_height*0.25) or y == int(self.terminal_height*0.75)-1:
                        stdscr.addstr(y,x,"─")

                # Fill left and right
                elif x == int(self.terminal_width*0.25) or x == int(self.terminal_width*0.75)-1:
                    stdscr.addstr(y,x,"│")

    def display_score(self):
        self.stdscr.addstr(int(self.terminal_height*0.9),int(self.terminal_width*0.25), f"Score: {self.score}")
                        
    def valid_position(self):
        """Verify if the snake is in a valid position"""

        for i in range(len(self.snake.body)):
            for j in range(i+1, len(self.snake.body)):
                if self.snake.body[i] == self.snake.body[j]:
                    self.playing = False
                    print("Game over!")
                    return
                
    def eat_apple(self):
        if (self.apple.x, self.apple.y) in self.snake.body:
            self.apple.x, self.apple.y = self.apple.create_apple()
            self.score +=1
            self.apple.counter -=1
            return True
        
        return False

    def render(self, stdscr):
        self.playing = True
        stdscr.nodelay(True)  # Non-blocking input
        stdscr.keypad(True)  # Enable arrow key input
        curses.curs_set(0)  # Hide cursor

        while self.playing:
            stdscr.clear()  # Clear screen before drawing
            self.display_board(stdscr)  # Draw the board
            self.display_score()
            self.stdscr.addstr(int(self.terminal_height*0.9),int(self.terminal_width*0.3), "Quit by pressing q", curses.A_BOLD)
            self.snake.display()  # Draw the snake
            if not (self.apple.counter > 0):
                self.apple.x, self.apple.y = self.apple.create_apple()
                self.apple.counter += 1

            self.apple.display_apple(self.apple.x, self.apple.y)

            key = stdscr.getch()  # Get user input

            # Handle movement keys
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
                break

            self.snake.move()  # Move the snake
            if self.eat_apple():
                 self.snake.grow() 
            self.valid_position()  # Check collisions

            stdscr.refresh()  # Refresh screen
            curses.napms(100)  # Delay to slow down animation

        stdscr.nodelay(False)  # Reset blocking input when game stops


