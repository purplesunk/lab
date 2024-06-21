def find_min(nums):
    minimum = float("inf")
    for num in nums:
        if num < minimum:
            minimum = num

    return minimum
