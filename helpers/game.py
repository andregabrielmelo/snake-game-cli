from helpers.snake import Snake
import os, random, datetime, curses

class Game:
    def __init__(self, height, width): 
        self.height: int = height
        self.width: int = width
        self.snake = Snake(self.height, self.width)
    
    def display_board(self, stdscr):
        """Function that displays the board of the game"""

        for y in range(int(self.height*0.25), int(self.height*0.75)):
            for x in range(int(self.width*0.25), int(self.width*0.75)):
                # Fill top left edge
                if y == int(self.height*0.25) and x == int(self.width*0.25):
                        stdscr.addstr(y,x,"┌ ")
                
                # Fill top right edge
                elif y == int(self.height*0.25) and x == int(self.width*0.75)-1:
                        stdscr.addstr(y,x,"┐")

                # Fill bottom left edge
                elif y == int(self.height*0.75)-1 and x == int(self.width*0.25):
                        stdscr.addstr(y,x,"└")

                # Fill bottom right edge
                elif y == int(self.height*0.75)-1 and x == int(self.width*0.75)-1:
                        stdscr.addstr(y,x,"┘")
                
                # Fill top and bottom
                elif y == int(self.height*0.25) or y == int(self.height*0.75)-1:
                        stdscr.addstr(y,x,"─")

                # Fill left and right
                elif x == int(self.width*0.25) or x == int(self.width*0.75)-1:
                    stdscr.addstr(y,x,"│")
                    
    def valid_position(self):
        """Verify if the snake is in a valid position"""

        for i in range(len(self.snake.body)):
            for j in range(i+1, len(self.snake.body)):
                if self.snake.body[i] == self.snake.body[j]:
                    self.playing = False
                    print("Game over!")
                    return

    def render(self, stdscr):
        self.playing = True
        stdscr.nodelay(True)  # Non-blocking input
        stdscr.keypad(True)  # Enable arrow key input
        curses.curs_set(0)  # Hide cursor

        while self.playing:
            stdscr.clear()  # Clear screen before drawing
            self.display_board(stdscr)  # Draw the board
            self.snake.display(stdscr)  # Draw the snake

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
                break

            self.snake.move()  # Move the snake
            self.valid_position()  # Check collisions

            stdscr.refresh()  # Refresh screen
            curses.napms(100)  # Delay to slow down animation

        stdscr.nodelay(False)  # Reset blocking input when game stops


