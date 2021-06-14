# Write a class Product that has three attributes:

# type
# name
# price

# Then create a class ProductStore, which will have some Products
# and will operate with all products in the store.
# All methods, in case they can’t perform its action,
# should raise ValueError with appropriate error information.

# Tips: Use aggregation/composition concepts while
# implementing the ProductStore class.
# You can also implement additional classes
# to operate on a certain type of product, etc.

# Also, the ProductStore class must have the following methods:

# add(product, amount) - adds a specified quantity of
# a single product with a predefined price premium
# for your store(30 percent)
# set_discount(identifier, percent, identifier_type=’name’)
# - adds a discount for all products specified
# by input identifiers (type or name).
# The discount must be specified in percentage
# sell_product(product_name, amount) - removes a particular
# amount of products from the store if available,
# in other case raises an error. It also increments income if the sell_product method succeeds.
# get_income() - returns amount of many earned
# by ProductStore instance.
# get_all_products() - returns information about
# all available products in the store.
# get_product_info(product_name) - returns a tuple
# with product name and amount of items in the store.


class Product:
    def __init__(self, type, name, price):
        """створення класу продуктів"""
        self.type = type
        self.name = name
        # перевірка, щоб ціна не була коректно введена
        try:
            if int(price) < 0:
                print(f'Ціна не може бути від\'ємним значенням. \n'
                      f'Якщо не виправите, то ціна цього товару — 0 грн. \n\n')
                self.price = 0
            else:
                self.price = round(float(price), 2)
        except ValueError:
            print(f'Ціна має бути введена цифрами. \n'
                  f'Якщо не виправите, то ціна цього товару — 0 грн.\n\n')
            self.price = 0


class ProductStore(Product):
    def __init__(self):
        self.product_list = []
        self.total_income = 0

    def add(self, product, amount):
        """додавання продукту до магазину зі знижкою у 30%"""
        # перевірка, щоб кількість була коректно введена
        try:
            if int(amount) < 0:
                print(f'Кількість товару не може бути менше нуля. \n'
                      f'Якщо не виправите, то к-ть товару — 0 штук (відсутній у магазині).\n\n')
                amount = 0
            # виводимо характеристики доданого до магазину товару
            else:
                self.product_list.append({'type': product.type, 'name': product.name,
                                          'price': round(product.price * 0.7, 2), 'amount': amount})
                print(f'Новий продукт: {product.name} ({product.type}), '
                      f'ціна зі знижкою у 30%: {round(product.price * 0.7, 2)} грн. Кількість одиниць: {amount}.\n\n')
        except ValueError:
            print(f'Кількість товару має бути числом. \n'
                  f'Якщо не виправите, то к-ть товару — 0 штук.\n\n')

    def set_discount(self, identifier, percent, identifier_type='name'):
        """встановлення знижки на продукт"""
        # перевіряємо, щоб відсоток був коректно введений
        try:
            if int(percent) < 0:
                print(f'Знижка не може бути від\'ємним значенням. \n'
                      f'Якщо не виправите, то знижка на цей товар — 0%.\n\n')
                percent = 0
        except ValueError:
            print(f'Знижка має бути введена цифрами. \n'
                  f'Якщо не виправите, то знижка на цей товар — 0%.\n\n')
            percent = 0

        for product in self.product_list:
            if identifier in product[identifier_type]:
                product['price'] *= (1 - (percent / 100))
                product['price'] = round(product['price'], 2)
                # виводимо оновлені характеристики акційного товару
                print(f"Акційний продукт: {product['name']} ({product['type']}), "
                      f"ціна зі знижкою у {percent}%: {product['price']} грн. "
                      f"Кількість одиниць: {product['amount']}.\n\n")

    def sell_product(self, product_name, amount):
        """продаж продукту у магазині і підрахування прибутку"""
        # перевіряємо, щоб кількість товару була коректно введена
        try:
            if int(amount) < 0:
                print(f'Кількість проданого товару не може бути менше нуля. \n'
                      f'Якщо не виправите, то к-ть проданого товару — 0 штук.\n\n')
                amount = 0
        except ValueError:
            print(f'Кількість проданого товару має бути числом. \n'
                  f'Якщо не виправите, то к-ть проданого товару — 0 штук.\n\n')

        for product in self.product_list:
            if product['name'] == product_name:
                # пропрацьовуємо сценарій, коли товару достатньо
                if product['amount'] > amount:
                    product['amount'] -= amount
                    print(f"Проданий продукт: {product['name']} ({product['type']}). Проданих одиниць: {amount}.")
                    self.total_income += round(amount * product['price'], 2)
                    print(f"Прибуток магазину завдяки цій транзакції: {round(amount * product['price'], 2)} грн.\n\n")
                # пропрацьовуємо сценарій, коли товару менше, ніж треба
                elif product['amount'] > 0:
                    print(f"Товару {product['name']} ({product['type']}) лишилося менше ({product['amount']} одиниць), "
                          f"ніж хочуть покупці ({amount} одиниць). "
                          f"Тому продаємо лише цю кількість, що лишилася.")
                    self.total_income += round(product['amount'] * product['price'], 2)
                    print(f"Прибуток магазину завдяки цій транзакції: "
                          f"{round(product['amount'] * product['price'], 2)} грн.\n\n")
                    product['amount'] = 0
                # пропрацьовуємо сценарій, коли товару вже немає
                else:
                    print(f"Товару {product['name']} ({product['type']}) більше не лишилося. Тому він не продається.\n\n")

    def get_income(self):
        """показ прибутку"""
        return self.total_income

    def get_all_products(self):
        """показ усіх продуктів та інформації про них"""
        return self.product_list

    def get_product_info(self, product_name):
        """показ продукту та його кількості за іменем"""
        product_info = []
        for product in self.product_list:
            if product['name'] == product_name:
                product_info.append((product['name'], product['amount']))
        return product_info


# створюємо товари
product_1 = Product('Sport', 'Football T-Shirt', 100)
product_2 = Product('Food', 'Ramen', 1)

# відкриваємо магазин
store = ProductStore()

# завозимо створені товари
store.add(product_1, 10)
store.add(product_2, 300)

# оголошуємо акцію
store.set_discount('Food', 20, 'type')

# приклад, коли товару достатньо
store.sell_product('Ramen', 10)
# приклад, коли товару менше, ніж треба
store.sell_product('Ramen', 300)
# приклад, коли товару вже немає для продажу
store.sell_product('Ramen', 20)

# статистика по магазину та окремим товарам
print(f'Загальний прибуток магазину — {store.get_income()} грн.')
print(f'Всі товари, які продаються в магазині: {store.get_all_products()}.')
print(f"Інформація про залишки товару за запитом: {store.get_product_info('Ramen')}")
