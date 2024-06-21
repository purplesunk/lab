def double_string(string):
    doubled_string = []
    for c in string:
        doubled_string.append(c + c)

    return "".join(doubled_string)
