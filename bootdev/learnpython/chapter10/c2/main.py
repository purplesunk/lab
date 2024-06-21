def merge(dict1, dict2):
    new_dict = {}
    for key in dict1:
        if key in new_dict:
            new_dict[key] = new_dict[key] + dict1[key]
        else:
            new_dict[key] = dict1[key]

    for key in dict2:
        if key in new_dict:
            new_dict[key] = new_dict[key] + dict2[key]
        else:
            new_dict[key] = dict2[key]

    return new_dict

def total_score(score_dict):
    total_score = 0
    for key in score_dict:
        total_score = total_score + score_dict[key]

    return total_score
