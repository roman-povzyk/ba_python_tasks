# Create a function called make_country,
# which takes in a country’s name and capital
# as parameters. Then create a dictionary
# from those two, with ‘name’ as a key and ‘capital’
# as a parameter. Make the function print
# out the values of the dictionary to make
# sure that it works as intended.

dictionary = {}


def make_country(country, capital, a_dict=dictionary):
    a_dict.update({country: capital})
    return a_dict


print(make_country('Ukraine', 'Kyiv'))
print(make_country('India', 'New Dehli'))
print(make_country('USA', 'Washington'))
