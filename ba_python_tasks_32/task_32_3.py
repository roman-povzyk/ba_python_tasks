# Write a console application which takes as an input a city name
# and returns current weather in the format of your choice.
# For the current task, you can choose any weather API
# or website or use https://openweathermap.org

import requests
import sys

# визначаємо потрібну адресу
url = 'http://api.openweathermap.org/data/2.5/weather'


def main():
    if len(sys.argv) > 2:
        city_name = sys.argv[2]
    else:
        city_name = input('Введіть місто: ')
    payload = {
        'q': city_name,
        'units': 'metric',
        'appid': '8dbc1f1632d291ba019e27d4e08ea9fd',
        'lang': 'ua'
    }
    # перевіряємо успішність запиту
    response = requests.get(url, params=payload)
    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 404:
        print('Not Found.')

    # виводимо потрібну характеристику
    print(response.json()['weather'][0]['main'])


if __name__ == '__main__':
    main()
