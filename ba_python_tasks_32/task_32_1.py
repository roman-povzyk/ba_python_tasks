# Download and save to file robots.txt
# from wikipedia, twitter websites etc.

# підвантажуємо потрібну бібліотеку
import requests

# обираємо потрібну адресу
url = 'https://en.wikipedia.org/robots.txt'


def main():
    # перевіряємо успішність запиту
    response = requests.get(url)
    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 404:
        print('Not Found.')

    # зберігаємо текст у файл
    with open('robots.txt', 'w', encoding='utf-8') as filename:
        filename.write(response.text)


if __name__ == '__main__':
    main()
