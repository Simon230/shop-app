import sys, os

sys.path.append(os.path.abspath('model/'))

from product import Product
from product import Products
from product import Customer

def display_menu():
    print("Choose what to do :\n\n")
    print("1) Create a new product")
    print("2) Buy a product")
    print("3) List products")
    print("0) Display this menu")

def create_product():
    '''
    '''
    product_name = input('Enter a product name...\t')
    product_price = input('Enter a product price...\t')
    new_product = Product(name = product_name, price = product_price)
    products.add_product(product=new_product)


if __name__ == "__main__":

    products = Products("dev")
    customer1 = Customer(name = "Toto")

    display_menu()
    while (True):
        input_user = input("Your choice...\t")
        print(f"input_user = {input_user}")
        if (input_user == '1'):
            print("You are going to create a new product: ")
            create_product()
        elif (input_user == '2'):
            print("You are going to buy a product")
        elif (input_user == '3'):
            print("All existing product")
            products.list_products()
        elif (input_user == '0'):
            print("Exit!! See you soon")
            break
        else:
            print("You didn't enter a correct choice. Try again")
            display_menu()