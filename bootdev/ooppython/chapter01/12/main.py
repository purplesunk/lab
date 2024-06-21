class Wall:
    def __init__(self, depth, height, width):
        self.depth = depth
        self.width = width
        self.height = height
        self.volume = depth * height * width
