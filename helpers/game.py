from helpers.snake import Snake
import datetime
import os

class Game:
    def __init__(self, height, width): 
        self.height: int = height
        self.width: int = width
        self.snake = Snake([(1, 1), (1, 3), (2, 1), (3, 1)], "UP")

    def board(self):
        """Create list that represents the board of the game"""

        board = []
        for i in range(self.height):
            for j in range(self.width):
                
                    # For edges +
                if ((i == 0 and j == 0) or 
                    (i == 0 and j == (self.width - 1)) or
                    (i == (self.height - 1) and j == 0) or
                    (i == (self.height - 1) and j == (self.width - 1))):
                    board.insert((i * self.width) + j,"+")

                # Top and bottom border -
                elif (i == 0 or i == self.height - 1):
                    board.insert((i * self.width) + j,"-")
                
                # Left and right border |
                elif (j == 0 or j == self.width - 1):
                    board.insert((i * self.width) + j,"|")
                
                # Empty space inside the board
                else:
                    board.insert((i * self.width) + j," ")
        
        return board

    def render(self):
        print(self.snake.body)
        # Show game Board
        board = self.board()
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) == self.snake.head():
                    print("o",end="")
                    continue
                    
                if (i, j) in self.snake.body and (i, j) != self.snake.head(): 
                    print("x",end="")
                    continue

                print(board[(i * self.width) + j], end="")
                if j == self.width-1: print()
        
        lastTimeRendered = datetime.datetime.now()
        
        self.snake.move()
        while True:
            if ((lastTimeRendered + datetime.timedelta(0,1)) < datetime.datetime.now()):
                os.system("clear")
                self.render()
                break
            

