list_version = [['665587', 2], ['669532', 1], ['669537', 2], ['669532', 1], ['665587', 1]]


def element_count(list_version):
    unique_values = set(map(tuple, list_version))
    return [[id, version, list_version.count([id, version])] for id, version in unique_values]


if __name__ == "__main__":
    print(element_count(list_version))
