import random, curses

class Snake:
    def __init__(self, board_height, board_width, stdscr):
        self.direction: str = "UP"
        self.board_height: int = board_height
        self.board_width: int = board_width
        self.stdscr: curses.window = stdscr
        self.body: list[tuple] = self.create_snake()

    def create_snake(self) -> list[tuple]:
        """Generate a random snake body"""

        # Pick random x point within board
        x: int = random.randint(int(self.board_width*0.25)+5, int(self.board_width*0.75)-5)

        # Pick random y point withing board
        y: int = random.randint(int(self.board_height*0.25)+5,int(self.board_height*0.75)-5)

        # The snake body will be continuos in the self.direction "UP", the first tuple being the head
        return [(x, y), (x,y+1), (x,y+2), (x,y+3)]
    
    def display(self) -> None:
        """Display snake body"""
        
        for x, y in self.body[1:]:
            if self.direction == "UP" or self.direction == "DOWN":
                self.stdscr.addstr(y, x, "║")  
            elif self.direction == "LEFT" or self.direction == "RIGHT":
                self.stdscr.addstr(y, x, "═")

    def move(self) -> None:
        """Move the snake and wrap around if it reaches the board's borders."""
        head_x, head_y = self.body[0]

        if self.direction == "UP":
            new_head = (head_x, head_y - 1)
            if new_head[1] < int(self.board_height * 0.25):  # Wrap around top border
                new_head = (head_x, int(self.board_height * 0.75) - 2)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + 1)
            if new_head[1] >= int(self.board_height * 0.75):  # Wrap around bottom border
                new_head = (head_x, int(self.board_height * 0.25) + 1)
        elif self.direction == "LEFT":
            new_head = (head_x - 1, head_y)
            if new_head[0] < int(self.board_width * 0.25):  # Wrap around left border
                new_head = (int(self.board_width * 0.75) - 2, head_y)
        elif self.direction == "RIGHT":
            new_head = (head_x + 1, head_y)
            if new_head[0] >= int(self.board_width * 0.75):  # Wrap around right border
                new_head = (int(self.board_width * 0.25) + 1, head_y)

        self.body.insert(0, new_head)  # Add new head at the front
        self.body.pop()  # Remove the last part (tail)
    
    def set_direction(self, direction: str) -> bool:
        self.direction: str = direction
        return True
    
    def grow(self) -> bool:
        """Extend the snake's body by adding a new segment at the tail position."""
        tail = self.body[-1]  # Get the last segment of the snake
        second_last = self.body[-2] if len(self.body) > 1 else tail  # Get second last segment

        # Determine the direction of growth by extending in the opposite direction
        if tail[0] == second_last[0]:  # Vertical growth
            new_segment = (tail[0], tail[1] + (tail[1] - second_last[1]))
        else:  # Horizontal growth
            new_segment = (tail[0] + (tail[0] - second_last[0]), tail[1])

        self.body.append(new_segment)  # Add new segment to the snake
        return True

    def head(self) -> tuple:
        return self.body[0]