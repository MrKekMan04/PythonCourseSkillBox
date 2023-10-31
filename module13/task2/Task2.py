import os.path


def gen_files_path(path: str = os.path.join(".")) -> list[str]:
    result = []
    for root, dirs, files in os.walk(path):
        result += [os.path.join(root, name) for name in files]
    return result


print(gen_files_path())
