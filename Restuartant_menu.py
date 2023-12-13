# # Create a Python program that simulates a restaurant's menu system. 

class Resturant:
    menu = {

        "Food" : "price",
        "Chicken": 300,
        "Beef": 599,
        "Potato":100,
        "Brayni": 250

    }

    def __init__(self):
        self.order_list = []

    def Order(self):
        user = input("Which think you like to order sir? ")
        if user.capitalize() in self.menu:
            print("Thanks for order sir! ")
            print(f"Here's your {user.upper()}. Hope you enjoy it.")
            self.order_list.append(user.capitalize())

        else:
            print("The food you orderd is not avalible in the menu. plese check the menu first.")

    def Total_price(self):
        Total_price = 0
        for item in self.order_list:
            Total_price += self.menu[item]
        
        return Total_price

r = Resturant()


print("\n*****/     WELCOME TO CHAUDHARY'S RESTURANT     /*****\n")    

while True:
    
    print('''
          Here's the option!
            1- check menu (m)
            2- order (r)
            3- Quit (q) 
           ''')
    user = input(">").lower()
    if user == 'm':
        for item in r.menu.keys():
            print(item, r.menu[item])
    elif user == 'r':
        r.Order()
    elif user == 'q':
        print("Thanks! for coming our restuartant")
        break
    else:
        print("please Select only given option.")

bill = r.Total_price()

if bill > 0:
    print(f"I hope you enoy your meal.Yout Total bill is {bill}$")
    print("Have a nice day ahead!")