valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line


def pair_document_with_format(doc_names, doc_formats):
    tuple_list = zip(doc_names, doc_formats)
    check_valid_format = lambda t: t[1] in valid_formats
    return filter(check_valid_format, tuple_list)

