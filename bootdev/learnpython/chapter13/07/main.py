def divide_list(nums, divisor):
    if divisor == 0:
        raise Exception("Can't divide by zero.")

    divided_list = []
    for num in nums:
        divided_list.append(num / divisor)

    return divided_list
