def area_sum(rectangles):
    result = 0
    for rec in rectangles:
        area = rec["height"] * rec["width"]
        result = result + area

    return result
