# Functionality of Phonebook application:

# Add new entries
# Search by first name
# Search by last name
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the  program

# The first argument to the application should
# be the name of the phonebook. Application
# should load JSON data, if it is present in the
# folder with application, else raise an error.
# After the user exits, all data should
# be saved to loaded JSON.

import json
import os
import sys


def search_if_phone_exist(number):
    if number in data_json.keys():
        return True
    else:
        return False


def search_by_content_exist():
    print('Введіть ім\'я, прізвище чи місто, які потрібно знайти: ')
    search_item = get_word_from_user()
    content_exist = 0
    for contact in data_json.values():
        for content in contact:
            if search_item == contact[content]:
                content_exist += 1
                print(f'Знайдено контактів:')
                print(f'№{content_exist} {contact}')
    if content_exist:
        return True
    else:
        print('Контакт з таким вмістом не знайдено')
        return False


def validate_word(word):
    if len(word) > 2:
        return word
    else:
        raise ValueError('Введіть щонайменше три символи')


def get_word_from_user():
    while True:
        try:
            return validate_word(input())
        except ValueError as error_msg_word:
            print(error_msg_word)


def validate_phone_number(number):
    if len(number) == 10 and number.isdigit():
        return number
    else:
        raise ValueError('Номер телефону повинен складатися з 10 цифр')


def get_phone_number_from_user():
    while True:
        try:
            return validate_phone_number(input('Телефон: '))
        except ValueError as error_msg:
            print(error_msg)


def add_new_contact():
    print('Запишіть новий контакт: ім\'я, прізвище, місто, телефон: ')

    new_first_name = get_word_from_user()
    new_last_name = get_word_from_user()
    new_city = get_word_from_user()
    new_phone_number = get_phone_number_from_user()

    if search_if_phone_exist(new_phone_number):
        print("""Такий телефон уже є у вашій книзі: 
редагуйте (№7) або видаліть (№8) його""")
    else:
        data_json[new_phone_number] = {
            'first_name': new_first_name,
            'last_name': new_last_name,
            'city': new_city
        }
        print('Даний контакт додано')


def search_by_fullname():
    print('Введіть ім\'я-прізвище, яке потрібно знайти: ')

    search_first_last_names = get_word_from_user()
    find_first_last_names = 0

    for contact in data_json.values():
        if search_first_last_names == f"{contact['first_name']} {contact['last_name']}" \
                or search_first_last_names == f"{contact['last_name']} {contact['first_name']}":
            find_first_last_names += 1
            print(f'Знайдено контактів: ')
            print(f'№{find_first_last_names} {contact}')

    if find_first_last_names == 0:
        print('Такого контакту не знайдено')


def search_by_phone():
    print('Введіть телефон, який потрібно знайти (10 цифр): ')

    search_phone_number = get_phone_number_from_user()
    find_phone_number = 0

    if search_if_phone_exist(search_phone_number):
        for phone in data_json.keys():
            if search_phone_number == phone:
                find_phone_number += 1
                print(f'Знайдено контактів з такими телефоном: ')
                print(f'№{find_phone_number} {data_json[phone]}')
    else:
        print('Такого контакту не знайдено')


def del_contact():
    print('Введіть номер телефону контакту, який потрібно видалити: ')

    search_for_del_phone = get_phone_number_from_user()

    if search_if_phone_exist(search_for_del_phone):
        del data_json[search_for_del_phone]
        print('Даний контакт видалено')
    else:
        print('Контакту з таким телефоном не знайдено')


def edit_contact():
    print('Запишіть номер телефону контакта, який хочете відредагувати: ')

    search_for_change_phone = get_phone_number_from_user()

    if search_if_phone_exist(search_for_change_phone):
        print('Запишіть оновлені дані контакту: ім\'я, прізвище, місто: ')
        change_first_name = get_word_from_user()
        change_last_name = get_word_from_user()
        change_city = get_word_from_user()

        for phone, contact in data_json.items():
            if search_for_change_phone == phone:
                contact['first_name'] = change_first_name
                contact['last_name'] = change_last_name
                contact['city'] = change_city
                print('Даний контакт змінено')
    else:
        print('Контакту з таким номером не знайдено')


def user_exit():
    with open('phonebook.json', 'w') as b_file:
        json.dump(data_json, b_file, ensure_ascii=False, indent=4)


def phonebook_func():
    answer = 0
    while answer != '9':
        # вибір дії у контактній книзі
        answer = input("""
        Що хочете зробити?
        '1'/'2' — додати новий контакт / шукати за ім\'ям
        '3'/'4' — шукати за прізвищем / шукати за ім\'ям-прізвищем
        '5'/'6' — шукати за номером телефону / шукати за містом
        '7'/'8' — видалити номер / редагувати контакт
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

        if answer == '1':  # введення нового контакту (№1)
            add_new_contact()
        # пошук за іменем (№2), прізвищем (№3) чи містом (№6)
        elif answer == '2' or answer == '3' or answer == '6':
            search_by_content_exist()
        elif answer == '4':  # пошук за іменем-прізвище (№4)
            search_by_fullname()
        elif answer == '5':  # пошук за телефоном (№5)
            search_by_phone()
        elif answer == '7':  # видалення контакту за номером (№7)
            del_contact()
        elif answer == '8':  # заміна контакту за номером (№8)
            edit_contact()
        elif answer == '9':  # вихід з програми (№9)
            user_exit()
            break

        # пропозиція зайти на новий цикл або вихід
        answer = input('Бажаєте провести ще одну дію? «так» — будь-яка клавіша, «вийти» — 9: ')
        if answer == '9':
            user_exit()


PB_DEF = 'phonebook.json'

if len(sys.argv) < 2:
    print('Не вказаний файл телефонної книги')
    file_name = PB_DEF
else:
    file_name = sys.argv[1].lower()
    if file_name.rfind('.json') == -1:
        file_name += '.json'
print(f'Використовується книга {file_name}')

try:
    if not os.path.isfile(file_name):
        raise OSError('Не можемо знайти json-файл у вказаній папці')

    with open(file_name, 'r') as a_file:
        data_json = json.load(a_file)

    phonebook_func()
    print(data_json)

except OSError as error_text:
    print(error_text)
