# Write a program that counts lines and characters in a file (similar to 'wc'
# Unix-utility, for additional info about it follow the link:
# https://www.geeksforgeeks.org/wc-command-linux-examples/
# or in case you have macOS or Linux —
# just call manual for this utility via command: 'man wc').

#  Create a Python module called 'mymod.py', which has three functions:

# count_lines(name) function that reads an input file and counts the number
# of lines in it (hint: file.readlines() does most of the work for you,
# and 'len' does the rest)
# count_chars(name) function that reads an input file and counts
# the number of characters in it (hint: file.read() returns a single string)
# test(name) function that calls both counting functions with a given input file­name.
# Such a filename generally might be passed-in, hard-coded, input with raw_input,
# or pulled from a command-line via the sys.argv list;
# for now, assume it’s a passed-in function argument.
# All three 'mymod.py' functions should expect a filename string to be passed in.


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
