class Product:
    def __init__(self, name, price=50, quantity=10):
        self.name = name
        self.price = price
        self.quantity = quantity

        

    def display_information(self):
        print(f"name = {self.name} - price = {self.price} - quantity = {self.quantity}")



class Products:
    def __init__(self,id)->None:
        self.id = id
        self.items = []
    
    def add_product(self, product):
        self.items.append(product)
        print(f"Product {product.name} created !")

    def list_products(self):
        print(f"{len(self.items)}")
        # for item in self.items:
        #     print(item.display_information())

class Customer:

    def __init__(self, name):
        self.name = name


    def buy(self, product):
        print('Buying a product...')
        if (product.quantity == 0):
            print(f"The stock for the product {product.name} is sold out!Come back later")
        else:
            print(f"Thanks for buying {product.name}. See you soon!")
            product.quantity = product.quantity - 1

    
