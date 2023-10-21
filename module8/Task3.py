site_template = {
    'html': {
        'head': {
            'title': 'Куплю/продам {0} недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на {0}',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}


def change_site_product_name(name: str, current_dict: dict):
    for key in current_dict.keys():
        if type(current_dict[key]) is str:
            if "{0}" in current_dict[key]:
                current_dict[key] = current_dict[key].format(name)
        elif type(current_dict[key]) is dict:
            change_site_product_name(name, current_dict[key])


sites = []

sites_count = int(input("Сколько сайтов: "))

for i in range(sites_count):
    new_site = site_template.copy()
    change_site_product_name(input("Введите название продукта для нового сайта: "), new_site)
    sites.append(new_site)

    print("\n".join([str(s) for s in sites]))
