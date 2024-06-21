def get_median_font_size(font_sizes):
    length = len(font_sizes)
    if font_sizes:
        return (sorted(font_sizes, reverse=True))[(length - (length % 2)) // 2]
    else:
        return None
