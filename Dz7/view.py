def main_menu():
    commands = ["Показать все контакты",
                "Открыть файл",
                "Сохранить файл",
                "Новый контакт",
                "5 Изменить контакт",
                "6 Удалить контакт",
                "Найти контакт",
                "Выйти из программы"]
    print("\nВыберете пункт меню: ")
    for i in range(len(commands)):
        print(f"\t{i+1}. {commands[i]}")
    user_input = int(input("\nВведите пункт меню:"))
    return user_input 

def show_contacts(phone_book: list):
    if len(phone_book) > 0:
        for item in phone_book:
            print(f"{item[0]} {item[1]} ({item[2]})")
    else:
        print(" Телефонная книга пустая или не загруженна")

def load_succes():
    print('Телефонная книга загруженна успешно')

def save_success():
    print('Телефонная книга сохранена успешно!')

def new_contact():
    name = input('Введите Имя и Фамилию контакта: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите коментарий к контакту: ')
    return name, phone, comment

def find_contact():
    search = input('Введите искомое значение: ')
    return search

def delete_user():
    name = input('Введите имя контакта: ')
    print('Контакт "{name}" удален')
    print('Извините, этого контакта не существует')
    return name

def update_user():
    name = input('Введите имя  контакта: ')
    phone = input('Введите новый номер телефона для контакта: ')
    print('Абонент "{name}" обновлен')
    print('Извините, этот контакт не существует')
    return name, phone