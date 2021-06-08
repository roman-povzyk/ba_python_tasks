# Create a simple prototype of a TV controller in Python.
# It’ll use the following commands:

# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel.
# Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel.
# If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel.
# If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N / 'name') - gets 1 argument - the number N or
# the string 'name' and returns "Yes",
# if the channel N or 'name' exists in the list, or "No" - in the other case.

# The default channel turned on before all commands is №1.

# Your task is to create the TVController class and methods described above.

# оголошуємо перелік каналів, які у нас є
CHANNELS = ['BBC / #1 / [0]', 'Discovery / #2 / [1]', 'TV1000 / #3 / [2]']


class TVController:
    # задаємо поточне значення на пульті
    my_channel = 0

    def __init__(self, channels):
        # отримуємо перелік наших каналів
        self.channels = channels

    def first_channel(self):
        # вмикаємо перший канал у списку (індекс: 0)
        TVController.my_channel = 0
        return self.channels[TVController.my_channel]

    def last_channel(self):
        # вмикаємо останній канал у списку (індекс: -1)
        TVController.my_channel = -1
        return self.channels[TVController.my_channel]

    def turn_channel(self, number):
        # додаємо задану кількість переключень
        TVController.my_channel += number
        if number >= 0:
            # перевіряємо, на який канал потрапили (не більше за довжину списку вперед - 1)
            while TVController.my_channel + 1 > len(self.channels):
                TVController.my_channel -= len(self.channels)
        else:
            # перевіряємо, на який канал потрапили (не менше за довжину списку назад)
            while TVController.my_channel < len(self.channels) * (-1):
                TVController.my_channel += len(self.channels)
        return self.channels[TVController.my_channel]

    def next_channel(self):
        # додаємо одне переключення вперед
        TVController.my_channel += 1
        # перевіряємо, на який канал потрапили (не більше за довжину списку вперед - 1)
        while TVController.my_channel + 1 > len(self.channels):
            TVController.my_channel -= len(self.channels)
        return self.channels[TVController.my_channel]

    def previous_channel(self):
        # додаємо одне переключення назад
        TVController.my_channel -= 1
        # перевіряємо, на який канал потрапили (не менше за довжину списку назад)
        while TVController.my_channel < len(self.channels) * (-1):
            TVController.my_channel += len(self.channels)
        return self.channels[TVController.my_channel]

    def current_channel(self):
        # показуємо, на якому каналі нині
        return self.channels[TVController.my_channel]

    def is_exist(self, question_channel):
        # визначаємо цифру чи літери отримали і відповідаємо щодо існування каналу
        question_channel = str(question_channel)
        if question_channel.isdigit():
            if int(question_channel) > len(self.channels):
                return 'No'
            else:
                return 'Yes'
        else:
            if question_channel not in self.channels:
                return 'No'
            else:
                return 'Yes'


controller = TVController(CHANNELS)

print(f'Наш список каналів: {controller.channels}')
print(f'Перший канал: {controller.first_channel()}')
print(f'Останній канал: {controller.last_channel()}')
print(f'Перемикаємо на n значень: {controller.turn_channel(1)}')
print(f'Наступний канал: {controller.next_channel()}')
print(f'Попередній канал: {controller.previous_channel()}')
print(f'Нинішній канал: {controller.current_channel()}')
print(f'Чи існує канал під номером N: {controller.is_exist(4)}')
print(f"Чи існує канал з іменем 'name': {controller.is_exist('BBC / #1 / [0]')}")
