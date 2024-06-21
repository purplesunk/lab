def count_enemies(enemy_names):
    enemies = {}
    for enemy in enemy_names:
        if enemy in enemies:
            enemies[enemy] = enemies[enemy] + 1
        else:
            enemies[enemy] = 1

    return enemies
