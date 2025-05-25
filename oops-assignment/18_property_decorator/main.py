class Product:
    def __init__(self, price):
        self._price = price  # private variable

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = new_price

    @price.deleter
    def price(self):
        del self._price

# Create an object
p = Product(100)

# Get the price
print(p.price)   # Output: 100

# Update the price
p.price = 200
print(p.price)   # Output: 200

# Delete the price
del p.price
