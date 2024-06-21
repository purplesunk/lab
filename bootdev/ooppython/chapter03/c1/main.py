class Calculator:
    def __init__(self):
        self.__result = 0

    def add(self, a):
        self.__result += a

    def subtract(self, a):
        self.__result -= a

    def multiply(self, a):
        self.__result *= a

    def divide(self, a):
        if a == 0:
            raise ValueError("Cannot divide by zero")

        self.__result /= a

    def modulo(self, a):
        if a == 0:
            raise ValueError("Cannot divide by zero")

        self.__result %= a

    def power(self, a):
        power_result = 1
        for _ in range(a):
            power_result *= self.__result

        self.__result = power_result

    def square_root(self):
        square_root = 0
        odd_number = 1
        number = self.__result
        while number > 0:
            number -= odd_number
            odd_number += 2
            square_root += 1

        self.__result = square_root


    def clear(self):
        self.__result = 0

    def get_result(self):
        return self.__result
