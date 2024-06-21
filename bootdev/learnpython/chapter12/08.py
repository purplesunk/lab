try:
    raise Exception('zero division')
except ZeroDivisionError as e:
    print("zero")
