class Human:
    def __init__(self, pos_x, pos_y, speed):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed

    def move_right(self):
        self._Human__pos_x += self._Human__speed

    def move_left(self):
        self._Human__pos_x -= self._Human__speed

    def move_up(self):
        self._Human__pos_y += self._Human__speed

    def move_down(self):
        self._Human__pos_y -= self._Human__speed

    def get_position(self):
        return (self._Human__pos_x, self._Human__pos_y)
