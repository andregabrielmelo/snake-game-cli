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
        self.previousDirection: str = "UP"

    def create_snake(self) -> list[dict[tuple, str]]:
        """Generate a snake starting at a safe position inside the board."""
        x = random.randint(self.board_width_start + 1, self.board_width_end - 1)
        y = random.randint(self.board_height_start + 4, self.board_height_end - 1)  # Ensure enough space

        return [
            {"position": (x, y), "direction": "UP"},
            {"position": (x, y - 1), "direction": "UP"},
            {"position": (x, y - 2), "direction": "UP"},
            {"position": (x, y - 3), "direction": "UP"},
        ]

    
    def generate(self) -> None:
        """Display snake body"""        

        for i in range(len(self.body)):
            previous_body_part = self.body[i-1 if i != 0 else i]
            body_part = self.body[i]

            # Display current body part
            y, x = body_part["position"]  # Extract coordinates
            self.stdscr.addstr(x, y, self.body_part(body_part["direction"], body_part["direction"]))

            if body_part["direction"] != previous_body_part["direction"]:
                previous_y, previous_x = previous_body_part["position"]
                self.stdscr.addstr(previous_x, previous_y, self.body_part(body_part["direction"], previous_body_part["direction"]))


    def body_part(self, direction: str, previous_direction: str) -> str:
        """Return snake body part based on direction and previous movement"""

        if direction != previous_direction:
            # Handle turns
            if previous_direction == "RIGHT" and direction == "DOWN":
                return "╗"
            elif previous_direction == "UP" and direction == "LEFT":
                return "╗"
            elif previous_direction == "RIGHT" and direction == "UP":
                return "╝"
            elif previous_direction == "DOWN" and direction == "LEFT":
                return "╝"
            elif previous_direction == "LEFT" and direction == "UP":
                return "╚"
            elif previous_direction == "DOWN" and direction == "RIGHT":
                return "╚"
            elif previous_direction == "UP" and direction == "RIGHT":
                return "╔"
            elif previous_direction == "LEFT" and direction == "DOWN":
                return "╔"
        else:
            # Handle straight movement
            if direction in ["UP", "DOWN"]:
                return "║"
            elif direction in ["LEFT", "RIGHT"]:
                return "═"

        return " "  # Default case, should not occur if logic is correct

        
    def move(self) -> None:
        """Move the snake and wrap around if it reaches the board's borders."""
        head_x, head_y = self.head()  # Get current head position

        if self.direction == "UP":
            new_head = (head_x, head_y - 1)
            if new_head[1] < self.board_height_start+1:  # Wrap around top border
                new_head = (head_x, self.board_height_end - 2)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + 1)
            if new_head[1] >= self.board_height_end-1:  # Wrap around bottom border
                new_head = (head_x, self.board_height_start + 1)
        elif self.direction == "LEFT":
            new_head = (head_x - 1, head_y)
            if new_head[0] < self.board_width_start+1:  # Wrap around left border
                new_head = (self.board_width_end - 2, head_y)
        elif self.direction == "RIGHT":
            new_head = (head_x + 1, head_y)
            if new_head[0] >= self.board_width_end-1:  # Wrap around right border
                new_head = (self.board_width_start + 1, head_y)

        # Add new head at the end of the body
        self.body.append({"position": new_head, "direction": self.direction})

        # Remove the first element (tail)
        self.body.pop(0)
    
    def set_direction(self, direction: str) -> bool:
        self.previousDirection: str = self.direction
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