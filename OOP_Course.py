class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # validando argumentos
        assert price >= 0, f"Price {price} não é maior ou igual a zero!"
        assert quantity >= 0, f"Quantity {quantity} não é maior ou igual a zero!"

        # definindo o objeto
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)

print(item1.calculate_total_price())
print(item2.calculate_total_price())
