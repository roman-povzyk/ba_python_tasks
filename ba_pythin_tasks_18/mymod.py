def count_lines(name):
    """Функція, яка рахує кількість рядків у файлі."""
    try:
        with open(name, 'r') as filename:
            lines = filename.readlines()
        return len(lines)
    except FileNotFoundError:
        print('На жаль, файл не знайдено.')


def count_chars(name):
    """Функція, яка рахує кількість знаків у файлі."""
    try:
        with open(name, 'r') as filename:
            string = filename.read()
        return len(string)
    except FileNotFoundError:
        print('На жаль, файл не знайдено.')


def test(name):
    """Функція, яка рахує кількість рядків і знаків у файлі."""
    return f'Рядків — {count_lines(name)}, знаків — {count_chars(name)}.'


if __name__ == '__main__':
    print(count_lines('sea.txt'))
    print(count_chars('sea.txt'))
    print(test('sea.txt'))
