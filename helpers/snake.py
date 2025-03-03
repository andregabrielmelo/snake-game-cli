class Snake:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction
  
    def move(self):
        if self.direction == "UP":
            self.body = [(x, y - 1) for x, y in self.body]
        elif self.direction == "DOWN":
            self.body = [(x, y + 1) for x, y in self.body]
        elif self.direction == "LEFT":
            self.body = [(x - 1, y) for x, y in self.body]
        elif self.direction == "RIGHT":
            self.body = [(x + 1, y) for x, y in self.body]
        return
    
    def rearrange_body(self, height):
        """Rearrange snake body if in the borders"""

        for i in range(len(self.body)):
            if self.body[i][1] == 0 and self.direction == "UP":
                self.body[i] = (self.body[i][0], height - 2)
            elif self.body[i][1] == height and self.direction == "DOWN":
                self.body[i] = (self.body[i][0], 1)
    
    def set_direction(self, direction):
        self.direction = direction

    def head(self, ):
        return self.body[0]