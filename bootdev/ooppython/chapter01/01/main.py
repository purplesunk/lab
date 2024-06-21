def destroy_walls(walls_health):
    for w in walls_health:
        if w <= 0:
            walls_health.remove(w)
    return walls_health
