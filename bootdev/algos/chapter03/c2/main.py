def remove_duplicates(nums):
    nodups = []
    for num in nums:
        if not num in nodups:
            nodups.append(num)
    return nodups
