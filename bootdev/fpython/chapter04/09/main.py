def list_files(current_filetree, current_path=""):
    file_paths = []
    for filetree in current_filetree:
        if current_filetree[filetree]:
            file_paths.extend(list_files(current_filetree[filetree], f"{current_path}/{filetree}"))
        else:
            file_paths.append(f"{current_path}/{filetree}")
    return file_paths
