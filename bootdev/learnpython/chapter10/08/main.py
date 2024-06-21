def get_most_common_enemy(enemies_dict):
    enemy_so_far = None
    max_so_far = float("-inf")
    for enemy in enemies_dict:
        if enemies_dict[enemy] > max_so_far:
            enemy_so_far = enemy
            max_so_far = enemies_dict[enemy]

    return enemy_so_far
