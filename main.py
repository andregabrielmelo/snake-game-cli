class Snake:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction
  
    def take_step(self, position):
        self.body = self.body[1:] + [position]
    
    def set_direction(self, direction):
        self.direction = direction

    def head(self, ):
        return self.body[-1]
  

class Apple: 
    ...

class Game:
    def __init__(self, height, width): 
        self.height: int = height
        self.width: int = width

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
        print("Height:", self.height)
        print("Width:", self.width)

        # Show game Board
        board = self.board()
        for i in range(self.height):
            for j in range(self.width):
                print(board[(i * self.width) + j], end="")
                if j == self.width-1: print()

        

                    
                

  
game = Game(10, 20)
game.render()