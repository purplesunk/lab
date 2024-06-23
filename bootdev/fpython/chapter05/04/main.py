def doc_format_checker_and_converter(conversion_function, valid_formats):
    def converter(filename, content):
        extension = filename.split(".")[-1]
        if extension in valid_formats:
            return conversion_function(content)
        raise ValueError("Invalid file format")
    return converter


# Don't edit below this line


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]
