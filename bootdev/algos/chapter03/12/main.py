def binary_search(target, arr):
    if not arr:
        return False
    median = len(arr) // 2
    if arr[median] == target:
        return True
    elif median == 0:
        return False
    elif arr[median] < target:
        return binary_search(target, arr[median:])
    else:
        return binary_search(target, arr[:median])
