def get_num_guesses(length):
    guesses = 0
    for i in range(1, length + 1):
        guesses += 26 ** i
    return guesses 
