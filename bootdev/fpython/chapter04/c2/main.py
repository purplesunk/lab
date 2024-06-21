def reverse_string(s):
    if not s:
        return ""
    return f"{s[-1:]}{reverse_string(s[:-1])}"
