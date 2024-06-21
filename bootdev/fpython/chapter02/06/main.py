def remove_invalid_lines(document):
    lines_list = document.split("\n")
    check_invalid_line = lambda s: not s.startswith("-")
    return "\n".join(list(filter(check_invalid_line, lines_list)))
