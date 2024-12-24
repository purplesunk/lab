def exponential_growth(n, factor, days):
    seq = []
    for i in range(days + 1):
        seq.append(n * (factor ** i))
    return seq
