class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg

        try:
            if int(msg) > 0:
                print('Введене число — більше нуля')
            elif int(msg) < 0:
                print('Введене число — менше нуля')
            elif int(msg) == 0:
                print('Введене число — нуль')
            else:
                raise Exception('Потрібно передати число.')

        except Exception as err_msg:
            try:
                with open('logs.txt', 'a') as file:
                    file.write(f'{str(err_msg)} \n')
            except PermissionError:
                print('Файл захищений від запису. Змініть його налаштування.')


my_file = CustomException('Stephen King')
