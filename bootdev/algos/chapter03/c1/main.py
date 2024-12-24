def count_names(list_of_lists, target_name):
    count = 0
    for name_list in list_of_lists:
        for name in name_list:
            if target_name == name:
                count += 1
    return count
