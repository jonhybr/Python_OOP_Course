import csv


class Item:
    pay_rate = 0.8  # Preço apos 20% de desconto
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # validando argumentos
        assert price >= 0, f"Price {price} não é maior ou igual a zero!"
        assert quantity >= 0, f"Quantity {quantity} não é maior ou igual a zero!"

        # definindo o objeto
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Ações
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
