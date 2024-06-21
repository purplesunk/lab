def reverse_array(items):
    reverse = []
    for i in range(len(items) - 1, -1, -1):
        reverse.append(items[i])

    return reverse
