def remove_duplicates(spells):
    spell_set = set()
    for spell in spells:
        spell_set.add(spell)

    learned_spells = []
    for spell in spell_set:
        learned_spells.append(spell)

    return learned_spells
