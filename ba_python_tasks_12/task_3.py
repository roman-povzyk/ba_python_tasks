# Create a Fraction class, which will represent all basic
# arithmetic logic for fractions (+, -, /, *)
# with appropriate checking and error handling

def smart_div(my_list):
    """функція, яка спрощує дроби,
    коли це необхідно, наприклад, 14/35 = 2/7"""
    nominator = int(my_list[0])
    denominator = int(my_list[1])
    # припускаємо, що найбільше спільне кратне — максимальне число у дробі
    least_common_divisor = max(abs(nominator), abs(denominator))
    print(least_common_divisor)
    # шукаємо справжнє спільне кратне, опускаючись до 2
    for search_item in range(least_common_divisor, 2, -1):
        if abs(nominator) % search_item == 0 and abs(denominator) % search_item == 0 and nominator != 0:
            nominator /= search_item
            denominator /= search_item
    # поправляємо знаки на випадок мінусових значень у знаменнику
    if nominator < 0 and denominator < 0:
        nominator *= -1
        denominator *= -1
    elif denominator < 0:
        denominator *= -1
    # вносимо спрощений дріб
    my_list.clear()
    my_list.append(int(nominator))
    my_list.append(int(denominator))
    # повертаємо спрощений дріб
    return my_list


def fraction_to_list(our_list_1, our_list_2):
    """функція, яка приводить задані дроби до списку зі спільними знаменниками
    (наприклад, 1/8 і 1/5 дає [5, 40, 8, 40])"""
    # формуємо два списки з отриманих дробів
    # перевіряємо адекватність дробів
    try:
        first_list = our_list_1.split('/')
        second_list = our_list_2.split('/')
        # створюємо один список з 4 елементів з двома дробами, приведеними до спільного знаменника
        final_list = []
        final_list.append(float(second_list[1]) * float(first_list[0]))
        final_list.append(float(second_list[1]) * float(first_list[1]))
        final_list.append(float(first_list[1]) * float(second_list[0]))
        final_list.append(float(second_list[1]) * float(first_list[1]))
        return final_list
    except ValueError:
        print('Значення дробів має бути введено цифрами. Перевірте ваші дані.')
    except ZeroDivisionError:
        print('Знаменник дробу не може дорівнювати нулю!')
    except IndexError:
        print('Перевірте уважно, чи ввели ви дріб. Введені некоректні дані.')
    except AttributeError:
        print('Перевірте, чи ввели ви дані у лапках. Інакше програма не працює.')
    except UnboundLocalError:
        print('Оскільки дані введено без лапок, програма не працюватиме.')


class Fraction:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('Невірний тип аргументу')
        # переводимо дріб у список
        our_fraction_in_list = fraction_to_list(self.value, other.value)
        # обчислюємо чисельник і знаменник
        try:
            answer_nominator = float(our_fraction_in_list[0] + float(our_fraction_in_list[2]))
            answer_denominator = float(our_fraction_in_list[1])
            # спрощуємо дріб
            final_answer = smart_div([answer_nominator, answer_denominator])
            if final_answer[-1] == 1:
                return Fraction(f'{final_answer[0]}')
            if final_answer[0] == 0:
                return Fraction(f'{final_answer[0]}')
            else:
                return Fraction(f'{final_answer[0]}/{final_answer[-1]}')
        except TypeError:
            print('Сума дробів не виведеться, оскільки ви ввели некоректні дані.')

    def __sub__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('Невірний тип аргументу')
        # переводимо дріб у список
        our_fraction_in_list = fraction_to_list(self.value, other.value)
        # обчислюємо чисельник і знаменник
        try:
            answer_nominator = float(our_fraction_in_list[0]) - float(our_fraction_in_list[2])
            answer_denominator = float(our_fraction_in_list[1])
            # спрощуємо дріб
            final_answer = smart_div([answer_nominator, answer_denominator])
            if final_answer[-1] == 1:
                return Fraction(f'{final_answer[0]}')
            if final_answer[0] == 0:
                return Fraction(f'{final_answer[0]}')
            else:
                return Fraction(f'{final_answer[0]}/{final_answer[-1]}')
        except TypeError:
            print('Різниця дробів не виведеться, оскільки ви ввели некоректні дані.')

    def __mul__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('Невірний тип аргументу')
        # переводимо дріб у список
        our_fraction_in_list = fraction_to_list(self.value, other.value)
        # обчислюємо чисельник і знаменник
        try:
            answer_nominator = float(our_fraction_in_list[0]) * float(our_fraction_in_list[2])
            answer_denominator = float(our_fraction_in_list[1]) * float(our_fraction_in_list[3])
            # спрощуємо дріб
            final_answer = smart_div([answer_nominator, answer_denominator])
            if final_answer[-1] == 1:
                return Fraction(f'{final_answer[0]}')
            if final_answer[0] == 0:
                return Fraction(f'{final_answer[0]}')
            else:
                return Fraction(f'{final_answer[0]}/{final_answer[-1]}')
        except TypeError:
            print('Множення дробів не виведеться, оскільки ви ввели некоректні дані.')

    def __truediv__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('Невірний тип аргументу')
        # переводимо дріб у список
        our_fraction_in_list = fraction_to_list(self.value, other.value)
        # обчислюємо чисельник і знаменник
        try:
            answer_nominator = int(our_fraction_in_list[0] * our_fraction_in_list[3])
            answer_denominator = int(our_fraction_in_list[1] * our_fraction_in_list[2])
            # спрощуємо дріб
            final_answer = smart_div([answer_nominator, answer_denominator])
            if final_answer[-1] == 1:
                return Fraction(f'{final_answer[0]}')
            if final_answer[0] == 0:
                return Fraction(f'{final_answer[0]}')
            else:
                return Fraction(f'{final_answer[0]}/{final_answer[-1]}')
        except TypeError:
            print('Ділення дробів не виведеться, оскільки ви ввели некоректні дані.')

    def __str__(self):
        return f"Відповідь: {self.value}"

    def __repr__(self):
        return self.__str__()


x = Fraction('1/2')
y = Fraction('-1/2')

print(x + y)
print(x - y)
print(x * y)
print(x / y)
