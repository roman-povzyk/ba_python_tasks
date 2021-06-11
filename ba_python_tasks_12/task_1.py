# Create a base class named Animal with a method called
# talk and then create two subclasses: Dog and Cat, and
# make their own implementation of the method talk be different.
# For instance, Dog’s can be to print ‘woof woof’,
# while Cat’s can be to print ‘meow’.

# Also, create a simple generic function,
# which takes as input instance of a Cat or Dog classes
# and performs talk method on input parameter.

class Animal:
    def __init__(self):
        pass

    def talk(self):
        raise NotImplementedError('Must be implemented by a sub class')


class Cat(Animal):
    def talk(self):
        print('Meow-meow!')


class Dog(Animal):
    def talk(self):
        print('Woof-woof!')


class YourDogTalk(Dog):
    def talk(self):
        msg = input('Введіть фразу для вашої собаки: ')
        print(f'Ваш пес каже: {msg}')


my_cat = Cat()
my_cat.talk()

my_dog = Dog()
my_dog.talk()

my_dog = YourDogTalk()
my_dog.talk()
