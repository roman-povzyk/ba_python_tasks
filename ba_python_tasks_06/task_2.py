# Create a function which takes as input two dicts
# with structure mentioned above,
# then computes and returns the total price of stock.

stock = {
    'banana': 6,
    'apple': 0,
    'orange': 32,
    'pear': 15
}
prices = {
    'banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3
}


def total_price(stock_dict, prices_dict):
    total_sum = 0
    total_dict = {key: stock_dict[key] * prices_dict.get(key, 0) for key in stock_dict.keys()}
    for value in total_dict.values():
        total_sum += value
    return total_sum


print(total_price(stock, prices))
