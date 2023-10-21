import os


def get_catalog_info(path: str) -> (int, int, int):
    total_catalog_weight = 0
    catalogs_count = 0
    files_count = 0

    for directory in os.listdir(path):
        if os.path.isdir(os.path.join(path, directory)):
            info = get_catalog_info(os.path.join(path, directory))
            total_catalog_weight += info[0]
            catalogs_count += info[1] + 1
            files_count += info[2]
        elif os.path.isfile(os.path.join(path, directory)):
            total_catalog_weight += os.path.getsize(os.path.join(path, directory))
            files_count += 1

    return total_catalog_weight, catalogs_count, files_count


catalog_info = get_catalog_info(input("Введите путь: "))

print(f"Размер каталога (в Кбайтах): {catalog_info[0] / 1024}\n"
      f"Количество подкаталогов: {catalog_info[1]}\n"
      f"Количество файлов: {catalog_info[2]}")
