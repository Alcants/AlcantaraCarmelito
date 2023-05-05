from itertools import product
from os import name, system
from getpass import getpass
from functools import reduce

class Product:
    name: str
    price: float

    def __init__(self, name, price):
        self.name = name
        self.price =price

class CartItem:
    product: Product
    quantity: int

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
       

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity

products : list [Product] = [
    Product('Tanduay', 120 ),
    Product('Red Horse', 160 ),
    Product('Fundador', 600),
    Product('Johnny Walker', 1600 ),
]

cart : list [CartItem] = []
    
def greetings():
    print(

   """
 __                __  __    __          __          
/ _     _  _  _   (_ ||__)  |__) /\ |\ ||  \ /\ |\ | 
\__)\)/(_||_)(_)  __)|| \   |   /--\| \||__//--\| \| 
          |                                                                                                                                                                                                                                        
   """
    )




def auth():
    while True:

        greetings()
        print('Please login to continue')

        print('\033[0;0m') # Reset colors

        username: str = input('Username : ')
        password: str = getpass('Password: ')

        if username == 'user' and password == '123456':

            print('\033[92mAuthentication Success! ')
            print('\033[0;0m') # Reset colors
            print('Press ENTER to continue ')

            input()
            return

        print('\033[91m Username or password not found!')
        print('Press ENTER to continue ')

        input()
        clear_terminal()



        
def clear_terminal ():
    if name == 'nt': # For windows
        system('cls')
    else: # For mac and linux( or posix )
        system('clear')

def show_products():
    while True: 
        print(
            """
            Select to add to cart!: 
            ======================================================
            """)
        for itx,i in enumerate(products):
            print(f'{itx+1}. {i.name}  - P{i.price}')

        print(
            """
            ======================================================
            [0] to Exit
            """)
        selected = input('Select item: ')

        if int(selected)  in range(len(products) + 1):
            print()
            qty = input('Quantity: ' )
            item = CartItem(product=products[int(selected)],quantity= int(qty))
            cart.append(item)
            return 
            
        print('\033[91m Invalid Input')
        print('\033[0;0m') # Reset colors
        print('Press ENTER to continue ')

        input()
        clear_terminal()

def update_products(item):
    units = int(input("Enter the number of products to add or subtract: "))

    # update products
    item["product"] += units
    print("The product level has been updated! The currents stock is:", item["products"])

    return item

def show_cart():
    print(
        """
        Your Cart: 
        ======================================================
        """)
    for itx,i in enumerate(cart):
        print(f'{itx}. {i.product.name} - ${i.product.price} - x{i.quantity} Subtotal : P{i.calculate_subtotal()}')

    print(
        """
        ======================================================
        [0] to Exit
        """)

    # Print Total
    print(f'P {reduce(lambda a,b: a + b.calculate_subtotal(),cart , 0.00)}')

    input()


def complete_transaction():
    pass

def display_main_menu():

    valid_input = True
    while valid_input:
        print(
            """
Select: 
======================================================
1. Show Products
2. View Cart
3. Complete Transaction

0. Exit
======================================================
    """
        )
        selected = input('Select an option: ')

        if selected == '1':
            show_products()

        elif choice == '2':
            # update the stock level of an product
            product_index = int(input("Enter the index of an product you want to update:"))  
            products[product_index] = update_products(products[product_index])
            
        elif selected == '3':
            show_cart()

        elif selected == '4':
            complete_transaction()
        elif selected == '0':
            exit()
        
        else:
            valid_input = False
            print('\033[91m Invalid Input')
            print('Press ENTER to continue ')

            input()
            if name == 'nt': # For windows
                system('cls')
            else: # For mac and linux( or posix )
                system('clear')


        

if __name__ == '__main__':
    auth()

    while True:
        display_main_menu()



