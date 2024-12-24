def does_name_exist(first_names, last_names, full_name):
    exists = False
    for fn in first_names:
        for ln in last_names:
            if fn + " " + ln == full_name:
                return True
    return exists
