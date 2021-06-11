class Product:
    def __init__(self, type, name, price):
        """створення класу продуктів"""
        self.type = type
        self.name = name
        try:
            if int(price) < 0:
                print(f'Ціна не може бути від\'ємним значенням. \n'
                      f'Якщо не виправите, то ціна цього товару — 0 грн.')
                self.price = 0
            else:
                self.price = round(float(price), 2)
        except ValueError:
            print(f'Ціна має бути введена цифрами. \n'
                  f'Якщо не виправите, то ціна цього товару — 0 грн.')
            self.price = 0


class ProductStore(Product):
    def __init__(self):
        self.product_list = []
        self.total_income = 0

    def add(self, product, amount):
        """додавання продукту до магазину зі знижкою у 30%"""
        try:
            if int(amount) < 0:
                print(f'Кількість товару не може бути менше нуля. \n'
                      f'Якщо не виправите, то к-ть товару — 0 штук.')
                amount = 0
            else:
                self.product_list.append({'type': product.type, 'name': product.name,
                                          'price': round(product.price * 0.7, 2), 'amount': amount})
        except ValueError:
            print(f'Кількість товару має бути числом. \n'
                  f'Якщо не виправите, то к-ть товару — 0 штук.')

    def set_discount(self, identifier, percent, identifier_type='name'):
        """встановлення знижки на продукт"""

        try:
            if int(percent) < 0:
                print(f'Знижка не може бути від\'ємним значенням. \n'
                      f'Якщо не виправите, то знижка на цей товар — 0%.')
                percent = 0
        except ValueError:
            print(f'Знижка має бути введена цифрами. \n'
                  f'Якщо не виправите, то знижка на цей товар — 0%.')
            percent = 0

        for product in self.product_list:
            for search_identifier in product[identifier_type]:
                if search_identifier == identifier:
                    product['price'] *= (1 - (percent / 100))
                    product['price'] = round(product['price'], 2)

    def sell_product(self, product_name, amount):
        """продаж продукту у магазині і підрахування прибутку"""
        try:
            if int(amount) < 0:
                print(f'Кількість проданого товару не може бути менше нуля. \n'
                      f'Якщо не виправите, то к-ть проданого товару — 0 штук.')
                amount = 0
        except ValueError:
            print(f'Кількість проданого товару має бути числом. \n'
                  f'Якщо не виправите, то к-ть проданого товару — 0 штук.')

        for product in self.product_list:
            if product['name'] == product_name:
                product['amount'] -= amount
                self.total_income = round(amount * product['price'], 2)

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


product_1 = Product('Sport', 'Football T-Shirt', 100)
product_2 = Product('Food', 'Ramen', 1.5)

store = ProductStore()

store.add(product_1, 10)
store.add(product_2, 300)

store.set_discount('Food', 50, 'type')
store.sell_product('Ramen', 10)

print(store.get_income())
print(store.get_all_products())
print(store.get_product_info('Ramen'))
