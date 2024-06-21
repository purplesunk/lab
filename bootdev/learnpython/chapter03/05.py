damage_one = 2
damage_two = 4
damage_three = 3
damage_four = -1
damage_five = 10
damage_six = 5

# Don't touch above this line


def triple_attack(slash_one, slash_two, slash_three):
    return slash_one + slash_two + slash_three


# Don't touch below this line

print("Getting damage for", damage_one, damage_two, "and", damage_three, "...")
print(triple_attack(damage_one, damage_two, damage_three), "points of damage dealt!")
print("=====================================")

print("Getting damage for", damage_four, damage_five, "and", damage_six, "...")
print(triple_attack(damage_four, damage_five, damage_six), "points of damage dealt!")
print("=====================================")
