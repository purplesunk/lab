def zipmap(keys, values):
    if not keys or not values:
        return {}
    new_dict = zipmap(keys[1:], values[1:])
    new_dict[keys[0]] = values[0]
    return new_dict
