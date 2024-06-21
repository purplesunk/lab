def fizzbuzz(start, end):
    for i in range(start, end):
        string = ""
        if i % 3 == 0:
            string = string + "fizz"
        if i % 5 == 0:
            string = string + "buzz"

        if string != "":
            print(string)
        else:
            print(i)


# Don't Touch Below This Line


def main():
    test(1, 100)
    test(5, 30)
    test(1, 15)


def test(start, end):
    print("Starting test")
    fizzbuzz(start, end)
    print("======================")


main()
