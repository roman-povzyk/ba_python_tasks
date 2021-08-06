# Download and save to file robots.txt
# from wikipedia, twitter websites etc.

import requests

url = 'https://en.wikipedia.org/robots.txt'


def main():
    response = requests.get(url)
    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 404:
        print('Not Found.')

    r = requests.get(url)
    with open('robots.txt', 'w', encoding='utf-8') as filename:
        filename.write(r.text)


if __name__ == '__main__':
    main()
