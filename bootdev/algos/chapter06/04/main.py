def verify_tsp(paths, dist, actual_path):
    path_distance = 0
    for i in range(len(actual_path) - 1):
        cityA = actual_path[i]
        cityB = actual_path[i + 1]
        path_distance += paths[cityA][cityB]
    if path_distance <= dist:
        return True
    else:
        return False
