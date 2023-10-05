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



if __name__ == "__main__":

    print("hello")
    products = Products("dev")
    #p1 = Product('pc', quantity=0)
    #p1.display_information()
    #c1 = Customer("Bob")
    #c1.buy(p1)
    #p1.display_information()

    while (True):
        display_menu()
        input_user = input("Your choice...\t")
        print(f"input_user = {input_user}")
        if (input_user == '1'):
            print("You are going to create a new product: ")
            new_product = Product('pc', quantity=5)
            products.add_product(product=new_product)
            
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
