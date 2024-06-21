def filename_getter(name_extension_tuples):
    extensions = {}
    for name_extension in name_extension_tuples:
        for extension in name_extension[1]:
            extensions[extension] = name_extension[0]

    return lambda file_extension: extensions.get(file_extension, "Unknown")
