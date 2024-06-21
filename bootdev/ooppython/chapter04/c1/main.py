class Rectangle:
    def __init__(self, length, width):
        self.__perimeter = (length * 2) + (width * 2)
        self.__area = length * width

    def get_area(self):
        return self.__area

    def get_perimeter(self):
        return self.__perimeter


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
