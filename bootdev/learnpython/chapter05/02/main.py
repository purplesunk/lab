def take_magic_damage(health, resist, amp, spell_power):
    damage = spell_power * amp
    new_health = health + (resist - damage)
    return new_health
