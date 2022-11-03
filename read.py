def get_data(src, separator):
    dicts_from_file = []
    name_symbol = ['Фамилия', 'Имя', 'Телефон', 'Комментарий']
    with open(src, 'r', encoding='utf-8') as file:
        for line in file:
            dicts_from_file.append(dict(zip(name_symbol, line.split(separator))))
    return dicts_from_file

