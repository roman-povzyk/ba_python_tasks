d = {}


def make_country(country, capital):
    d.update({country: capital})
    return d


print(make_country('Ukraine', 'Kyiv'))
print(make_country('India', 'New Dehli'))
