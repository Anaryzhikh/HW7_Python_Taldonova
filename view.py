
def user_command():
    num = int(input('Введите \n 1. Если вы хотите найти контакт: \n 2. Если вы хотите создать новый контакт: \n 3. Если вы хотите посмотреть все контаткы: \n 4. Если вы хотите завершить работу: \n'))
    if 0 < num < 5:
        return num
    else:
        print('Число введено неверно. Программа будет завершена')
        return 4

def find_contact():
    find_me = input('Введите фамилию или имя: ')
    return find_me

def create_contact():
    new_contact = {'id':''}
    new_contact['Фамилия'] = input('Введите фамилию: ')
    new_contact['Имя'] = input('Введите имя: ')
    while new_contact['Имя'] == '':
        new_contact['Имя'] = input('Введите имя: ')
    new_contact['Телефон'] = input('Введите телефон: ')
    new_contact['Комментарий'] = input('Добавьте комментарий: ')
    print(new_contact)
    return new_contact

from tabulate import tabulate

def print_all_contacts(data):
    data_to_print = []
    for i in range(len(data)):
        listik = list(data[i].values())
        listik.pop(0)
        data_to_print.append(listik)

    col_names = ["Фамилия", "Имя", "Телефон", "Комментарий"]
    print(tabulate(data_to_print, headers=col_names, tablefmt="fancy_grid", showindex="never"))



