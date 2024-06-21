def remove_nonints(nums):
    ints = []
    for num in nums:
        if type(num) == int:
            ints.append(num)

    return ints
