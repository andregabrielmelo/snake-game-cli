class Snake:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction
  
    def move(self):
        print("Before move:", self.body)
        if self.direction == "UP":
            self.body = [(x, y - 1) for x, y in self.body]
        elif self.direction == "DOWN":
            self.body = [(x, y + 1) for x, y in self.body]
        elif self.direction == "LEFT":
            self.body = [(x - 1, y) for x, y in self.body]
        elif self.direction == "RIGHT":
            self.body = [(x + 1, y) for x, y in self.body]

        print("After move:", self.body)
        return

    
    def set_direction(self, direction):
        self.direction = direction

    def head(self, ):
        return self.body[-1]