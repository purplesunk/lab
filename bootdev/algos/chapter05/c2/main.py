def num_countries_in_days(max_days, factor):
    time_left = max_days
    count = 0
    time_in_country = 1

    while (time_left - time_in_country) >= 0:
        count += 1
        time_left -= time_in_country
        time_in_country = time_in_country * factor

    return count
