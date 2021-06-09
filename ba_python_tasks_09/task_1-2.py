try:
    with open('myfile.txt') as file:
        text_from_file = file.read()
except FileNotFoundError:
    print('На жаль, файл не знайдено')
else:
    print(text_from_file)
