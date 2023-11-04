site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def get_key_value(find_key: str, pass_obj: dict, left_deep) -> object:
    if left_deep == 0:
        return None

    if find_key in pass_obj:
        return pass_obj[find_key]
    else:
        for obj_key in pass_obj.keys():
            if type(pass_obj[obj_key]) is dict:
                returned_value = get_key_value(find_key, pass_obj[obj_key], max_deep - 1)
                if returned_value is not None:
                    return returned_value
    return None


key = input("Введите искомый ключ: ")
has_deep = True if input("Хотите ввести максимальную глубину? Y/N: ").lower() == "y" else False
max_deep = int(input("Введите максимальную глубину: ")) if has_deep else float("inf")

print(f"Значение ключа: {get_key_value(key, site, max_deep)}")
