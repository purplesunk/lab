def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    sorted_left_side = merge_sort(nums[:mid])
    sorted_right_side = merge_sort(nums[mid:])
    return merge(sorted_left_side, sorted_right_side)


def merge(first, second):
    final = []
    i = 0
    j = 0
    while True:
        if i == len(first) and j == len(second):
            return final
        if i < len(first)  and j == len(second):
            final.append(first[i])
            i += 1
            continue
        if j < len(second) and i == len(first):
            final.append(second[j])
            j += 1
            continue
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1

