# Make a directory with 2 modules; make a function in one of them;
# then import this function in the other module and use that in your script of choice.


import random


# створюємо функцію для вгадування числа
def guess_number():
    comp_number = random.randint(1, 100)
    human_number = 0

    while comp_number != human_number:
        try:
            human_number = int(input('Введіть число від 1 до 100: \n'))
            if human_number < comp_number:
                print('Треба більше!')
            elif human_number > comp_number:
                print('Треба менше!')
            else:
                print('Вгадали!')
        except ValueError:
            print('Потрібно ввести число!')


# забороняємо використовувати функцію в інших файлах без виклику
if __name__ == '__main__':
    guess_number()
