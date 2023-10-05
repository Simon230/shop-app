class Product:
    def __init__(self, name, price=50):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product info \nname : {self.name} - price : {self.price}"


class Products:
    def __init__(self,id)->None:
        self.id = id
        self.items = []
    
    def add_product(self, product):
        self.items.append(product)
        print(f"Product {product} created !")

    def list_products(self):
        # print(f"{len(self.items)}")
        for item in self.items:
            print(item)

class Customer:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Customer : {self.name}"

    def buy(self, product):
        print('Buying a product...')
        print('Select the product you want to buy :')


    
