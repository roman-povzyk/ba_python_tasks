# Make a program that has some sentence (a string)
# on input and returns a dict containing all unique words
# as keys and the number of occurrences as values.

sentence = input('Введіть, будь ласка, своє речення: ')

symbols_list = ['.', ',', '!', '—', ':', ';', '?', '(', ')', '"', "'"]

for symbol in symbols_list:
    sentence = sentence.replace(symbol, '')

sentence = sentence.lower()

a_list = sentence.split(" ")
a_dict = {word: a_list.count(word) for word in a_list}

print(a_dict)
