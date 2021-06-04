import json
import os

try:
    if os.path.isfile(r'C:Users\User\PycharmProjects\ba_python_tasks\ba_python_tasks_08\phonebook.json'):
        with open('phonebook.json', 'r') as file:
            data = file.read()
            data_json = json.loads(data)
except OSError:
    print('Не можемо знайти ваш файл')


def phonebook_func():
    answer = 0
    while answer != '9':
        # вибір дії у контактній книзі
        answer = input("""
        Що хочете зробити?
        '1' — додати новий контакт
        '2' — шукати за ім'ям
        '3' — шукати за прізвищем
        '4' — шукати за ім'ям-прізвищем
        '5' — шукати за номером телефону
        '6' — шукати за містом
        '7' — видалити номер
        '8' — редагувати контакт
        '9' — вийти з телефонної книги
        Зробіть свій вибір: """)

        # захищаємо себе від рядкових даних та цифр не в діапазоні 1-9
        while True:
            if answer.isdigit():
                if int(answer) < 1 or int(answer) > 9:
                    answer = input('Введіть, будь ласка, число від 1 до 9: ')
                else:
                    break
            else:
                answer = input('Введіть, будь ласка, ЧИСЛО: ')

        # введення нового контакту (№1)
        if answer == '1':
            print('Запишіть новий контакт')
            new_first_name = input("Ім'я: ")
            new_last_name = input("Прізвище: ")
            new_city = input("Місто: ")
            new_phone_number = input("Телефон: ")

            data_json['phonebook'].append({
                "first_name": new_first_name,
                "last_name": new_last_name,
                "city": new_city,
                "phone_number": new_phone_number
            })

        # пошук за іменем (№2)
        elif answer == '2':
            search_first_name = input("Введіть ім'я, яке потрібно знайти: ")
            find_first_name = 0
            for name in data_json['phonebook']:
                if search_first_name == name['first_name']:
                    find_first_name += 1
                    print(f'Знайдено контактів з таким іменем:')
                    print(f'№{find_first_name} {name}')
            if find_first_name == 0:
                print('Такого контакту не знайдено')

        # пошук за прізвищем (№3)
        elif answer == '3':
            search_last_name = input("Введіть прізвище, яке потрібно знайти: ")
            find_last_name = 0
            for name in data_json['phonebook']:
                if search_last_name == name['last_name']:
                    find_last_name += 1
                    print(f'Знайдено контактів з таким прізвищем:')
                    print(f'{find_last_name} {name}')
            if find_last_name == 0:
                print('Такого контакту не знайдено')

        # пошук за іменем-прізвище (№4)
        elif answer == '4':
            search_first_last_names = input("Введіть ім'я-прізвище, яке потрібно знайти: ")
            find_first_last_names = 0
            for name in data_json['phonebook']:
                if search_first_last_names == f'{name["first_name"]} {name["last_name"]}' or search_first_last_names == f'{name["last_name"]} {name["first_name"]}':
                    find_first_last_names += 1
                    print(f"Знайдено контактів з такими ім'ям-прізвищем:")
                    print(f'{find_first_last_names} {name}')
            if find_first_last_names == 0:
                print('Такого контакту не знайдено')

        # пошук за телефоном (№5)
        elif answer == '5':
            search_phone_number = input("Введіть телефон, який потрібно знайти: ")
            find_phone_number = 0
            for name in data_json['phonebook']:
                if search_phone_number == name['phone_number']:
                    find_phone_number += 1
                    print(f"Знайдено контактів з такими телефоном:")
                    print(f'{find_phone_number} {name}')
            if find_phone_number == 0:
                print('Такого контакту не знайдено')

        # пошук за містом (№6)
        elif answer == '6':
            search_city = input("Введіть місто, яке потрібно знайти: ")
            find_city = 0
            for name in data_json['phonebook']:
                if search_city == name['city']:
                    find_city += 1
                    print(f"Знайдено контактів з такого міста:")
                    print(f'{find_city} {name}')

        # видалення контакту за номером (№7)
        elif answer == '7':
            search_for_del_phone = input("Введіть номер телефону контакту, який потрібно видалити: ")
            for name in data_json['phonebook']:
                if search_for_del_phone == name['phone_number']:
                    data_json['phonebook'].remove(name)

        # заміна контакту за номером (№8)
        elif answer == '8':

            search_for_change_phone = input('Запишіть номер телефону контакта, який хочете відредагувати: ')
            change_first_name = input("Нове ім'я: ")
            change_last_name = input("Нове прізвище: ")
            change_city = input("Нове місто: ")
            change_phone_number = input("Новий телефон: ")

            for name in data_json['phonebook']:
                if search_for_change_phone == name['phone_number']:
                    name["first_name"] = change_first_name
                    name["last_name"] = change_last_name
                    name["city"] = change_city
                    name["phone_number"] = change_phone_number

        # вихід з програми (№9)
        elif answer == '9':
            with open('phonebook.json', 'w') as file:
                json.dump(data_json, file, ensure_ascii=False, indent=4)
            break

        # пропозиція зайти на новий цикл або вихід
        answer_end = input('Бажаєте провести ще одну дію? «так» — будь-яка клавіша, «вийти» — 9: ')
        if answer_end == '9':
            with open('phonebook.json', 'w') as file:
                json.dump(data_json, file, ensure_ascii=False, indent=4)
            break


phonebook_func()
print(data_json)
