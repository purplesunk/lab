def sum_nested_list(lst):
    if not lst:
        return 0
    if isinstance(lst[0], list):
        return sum_nested_list(lst[0]) + sum_nested_list(lst[1:])
    return lst[0] + sum_nested_list(lst[1:])
