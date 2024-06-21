def join_strings(strings):
    joined_string = ""
    for string in strings:
        if joined_string == "":
            joined_string = string
        else:
            joined_string = joined_string + f",{string}"

    return joined_string
