# Download all comments from a subreddit
# of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
# As a result, store all comments in chronological order in JSON and dump it to a file.

# підключаємо потрібні бібліотеки
import requests
import json

# визначаємо потрібну адресу
url = 'https://api.pushshift.io/reddit/comment/search/'


def main():
    # перевіряємо успішність запиту
    response = requests.get(url)
    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 404:
        print('Not Found.')

    # призначаємо змінні для роботи
    our_json = response.json()
    id = []

    # зберігаємо дані файлу
    with open('data.json', 'r') as a_file:
        data_json = json.load(a_file)

    # отримуємо коментарі обраного підрозділу і формуємо список id
    for i in our_json.values():
        for j in range(len(i)):
            if i[j]['subreddit'] == 'AskReddit':
                id.append(i[j]['id'])

    # сортуємо id, щоб отримати хронологічний порядок
    id.sort()

    # завантажуємо коментарі у хронологічному порядку у JSON
    for i in our_json.values():
        for j in range(len(i)):
            for k in id:
                if k in i[j]['id']:
                    print(i[j])
                    data_json['data'].append(i[j])

    # записуємо наші відсортовані коментарі у файл
    with open('data.json', 'w') as b_file:
        json.dump(data_json, b_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
