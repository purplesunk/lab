def calculate_experience_points(level):
    xp = 0
    for i in range(0, level):
        xp = xp + (i * 5)
    return xp
