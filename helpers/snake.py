import random, curses

class Snake:
    def __init__(self, stdscr: curses.window, board_height_start: int, board_height_end: int, board_width_start: int, board_width_end: int, direction: str = "UP"):
        self.stdscr: curses.window = stdscr
        self.board_height_start: int = int(board_height_start)
        self.board_height_end: int = int(board_height_end)
        self.board_width_start: int = int(board_width_start)
        self.board_width_end: int = int(board_width_end)
        self.direction: str = direction
        self.body: list[dict[tuple, str]] = self.create_snake()
        self.direction: str = "UP"

    def create_snake(self) -> list[dict[tuple, str]]:
        """Generate a random snake body"""

        x: int = random.randint(self.board_width_start, self.board_width_end) # Pick random x point within board
        y: int = random.randint(self.board_height_start, self.board_height_end) # Pick random y point withing board
        return [
            {
                "position": (x, y),
                "direction": "UP"
            },
            {
                "position": (x, y+1),
                "direction": "UP"
            },
            {
                "position": (x, y+2),
                "direction": "UP"
            },
            {
                "position": (x, y+3),
                "direction": "UP"
            },
        ]
    
    def generate(self) -> None:
        """Display snake body"""
        max_y, max_x = self.stdscr.getmaxyx()  # Get screen size
        
        for body_part in self.body:
            y, x = body_part["position"]  # Extract coordinates
            
            self.stdscr.addstr(x, y, self.body_part(body_part["direction"]))

    def body_part(self, direction: str) -> str:
        """Return snake body part"""

        if direction == "UP" or direction == "DOWN":
            return "║"
        elif direction == "LEFT" or direction == "RIGHT":
            return "═"
        
    def move(self) -> None:
        """Move the snake and wrap around if it reaches the board's borders."""
        head_x, head_y = self.head()  # Get current head position

        if self.direction == "UP":
            new_head = (head_x, head_y - 1)
            if new_head[1] < self.board_height_start:  # Wrap around top border
                new_head = (head_x, self.board_height_end - 2)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + 1)
            if new_head[1] >= self.board_height_end:  # Wrap around bottom border
                new_head = (head_x, self.board_height_start + 1)
        elif self.direction == "LEFT":
            new_head = (head_x - 1, head_y)
            if new_head[0] < self.board_width_start:  # Wrap around left border
                new_head = (self.board_width_end - 2, head_y)
        elif self.direction == "RIGHT":
            new_head = (head_x + 1, head_y)
            if new_head[0] >= self.board_width_end:  # Wrap around right border
                new_head = (self.board_width_start + 1, head_y)

        # Add new head at the end of the body
        self.body.append({"position": new_head, "direction": self.direction})

        # Remove the first element (tail)
        self.body.pop(0)
    
    def set_direction(self, direction: str) -> bool:
        self.direction: str = direction
        return True
    
    def grow(self) -> bool:
        """Extend the snake's body by adding a new segment at the tail position."""
        tail = self.body[0]["position"]  # Get the last segment of the snake
        second_last = self.body[1]["position"] if len(self.body) > 1 else tail  # Get second last segment

        # Determine the direction of growth by extending in the opposite direction
        if tail[0] == second_last[0]:  # Vertical growth
            new_segment = {"position": (tail[0], tail[1] + (tail[1] - second_last[1])), "direction": self.direction}
        else:  # Horizontal growth
            new_segment = {"position":(tail[0] + (tail[0] - second_last[0]), tail[1]), "direction": self.direction}

        self.body.insert(0, new_segment)  # Add new segment to the snake
        return True

    def head(self) -> tuple:
        return self.body[-1]["position"]