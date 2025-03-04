import random, curses

class Snake:
    def __init__(self, height, width):
        self.direction = "UP"
        self.height = height
        self.width = width
        self.body = self.create_snake()

    def create_snake(self):
        """Generate a random snake body"""

        # Pick random x point
        x = random.randint(int(self.width*0.25)+5, int(self.width*0.75)-5)

        # Pick random y
        y = random.randint(int(self.height*0.25)+5,int(self.height*0.75)-5)

        # The snake body will be continuos in the self.direction "UP", the first tuple being the head
        return [(x, y), (x,y+1), (x,y+2), (x,y+3)]
    
    def display(self, stdscr):
        # Display head
        stdscr.addstr(self.body[0][1], self.body[0][0], "O")  # Use y first (row), then x (col)
        
        # Display body
        for x, y in self.body[1:]:
            try:
                stdscr.addstr(y, x, "x")  # Use y first (row), then x (col)
            except curses.error:
                pass  # Prevent crashes if out of bounds

    def move(self):
        """Move the snake and wrap around if it reaches the board's borders."""
        head_x, head_y = self.body[0]

        if self.direction == "UP":
            new_head = (head_x, head_y - 1)
            if new_head[1] < int(self.height * 0.25):  # Wrap around top border
                new_head = (head_x, int(self.height * 0.75) - 2)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + 1)
            if new_head[1] >= int(self.height * 0.75):  # Wrap around bottom border
                new_head = (head_x, int(self.height * 0.25) + 1)
        elif self.direction == "LEFT":
            new_head = (head_x - 1, head_y)
            if new_head[0] < int(self.width * 0.25):  # Wrap around left border
                new_head = (int(self.width * 0.75) - 2, head_y)
        elif self.direction == "RIGHT":
            new_head = (head_x + 1, head_y)
            if new_head[0] >= int(self.width * 0.75):  # Wrap around right border
                new_head = (int(self.width * 0.25) + 1, head_y)

        self.body.insert(0, new_head)  # Add new head at the front
        self.body.pop()  # Remove the last part (tail)


    
    def set_direction(self, direction):
        self.direction = direction

    def head(self, ):
        return self.body[0]