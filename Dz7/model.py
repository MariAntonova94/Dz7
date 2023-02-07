phone_book = []
path = 'phone_book.txt'

def get_phone_book():
    global phone_book
    return phone_book

def update_phone_book(contact: list):
    global phone_book
    phone_book.append(contact)

def open_phone_book():
    global phone_book
    global path 
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for line in data:
            phone_book.append(line.strip().split(';'))

def save_phone_book():
    global phone_book
    global path 
    data = []
    for line in phone_book:
        data.append(';'.join(line))
    with open(path, 'w', encoding='UTF-8') as file:
        data = file.write('\n'.join(data))

def search_contact(search: str):
    global phone_book
    search_results = []
    for line in phone_book:
        for field in line:
            if search in field:
                search_results.append(line)
                break
   
    return search_results

def delete_user():
    name = input('Введите имя контакта: ')
    if name in delete_user:
        delete_user.pop(name)
        print('Контакт "{}" удален'.format(name))
    else:
        print('Извините, этого абонента не существует')
    return delete_user


def update_user():
    name = input('Введите имя  контакта: ')
    phone= input('Введите новый номер телефона для контакта: ')
    if name in phone:
        update_user[name] = phone
        print('Абонент "{}" обновлен'.format(name))
    else:
        print('Извините, этот контакт не существует')
    return update_user