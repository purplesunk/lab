def markdown_to_text_decorator(func):
    def wrapper(*args, **kargs):
        new_args = list(map(convert_md_to_txt, args))
        new_kargs = dict()
        for k, v in kargs.items():
            new_kargs[k] = convert_md_to_txt(v)
        return func(*new_args, **new_kargs)
    return wrapper

# don't touch below this line


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)
