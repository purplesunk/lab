def power_set(input_set):
    if not input_set:
        return [[]]
    subsets = []
    r = power_set(input_set[1:])
    for subset in r:
        subsets.append([input_set[0]] + subset)
        subsets.append(subset)
    return subsets
