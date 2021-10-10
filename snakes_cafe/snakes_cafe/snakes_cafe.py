"""

"""

# Food Courses 

appetizers = ["Wings", "Cookies", "Spring "]

entrees = ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]

desserts = ["Ice Cream", "Cake", "Pie"]

drinks = ["Coffee", "Tea", "Unicorn Tears"]

menu = [appetizers, entrees, desserts, drinks]

def welcome():
    """
    This function prints the welcoming message and presents menu items to users. 
    Then it allowes the user to order courses and finally prints out their order to them.
    return: Cafe User Interface
    """
    print(
        "************************************** \n**    Welcome to the Snakes Cafe!   **\n**    Please see our menu below.    **\n**                                  **\n** To quit at any time, type \"quit\" **\n**************************************"
    )
    print()

    print(
        "Appetizers\n----------" 
    )
    for appetizer in appetizers:
        print(appetizer)
    print()

    print(
        "Entrees\n----------" 
    )
    for entree in entrees:
        print(entree)
    print()

    print(
        "Desserts\n----------" 
    )
    for dessert in desserts:
        print(dessert)
    print()

    print(
    "Drinks\n----------" 
    )
    for drink in drinks:
        print(drink)
    print()

    full_order = []

    print(
        "***********************************\n** What would you like to order? **\n***********************************"
    )

    while True:

        response = input()
        if response != "quit":
            if len(full_order) == 0:
                full_order.append({response.lower() : 1})
                print(f"** 1 order of {response} have been added to your meal **")
            else:
                check = False
                for orders in full_order:
                    for key, value in orders.items():
                        if (response.lower() == key):
                            orders[key] = value + 1
                            print()
                            print(f"** {orders[key]} order of {response} have been added to your meal **")
                            check = True

                            continue

                if check == False:
                    full_order.append({response.lower() : 1})
                    print()
                    print(f"** 1 order of {response} have been added to your meal **")

        else: 
            if len(full_order) == 0:
                print()
                print("You did not order anything.")
            else:
                print()
                print("Your meal includes:")
                for orders in full_order:
                    for key, value in orders.items():
                            for courses in menu:
                                if key.capitalize() in courses:
                                    if value == 1:
                                        print(f"{value} order of {key}")
                                        break
                                    else:
                                        print(f"{value} orders of {key}")
                                        break

                            else:
                                if value == 1:
                                    print(f"{value} order of {key}, this order will take longer time to prepare since not all ingredients are currently available.")
                                    continue
                                else:
                                    print(f"{value} orders of {key}, this order will take longer time to prepare since not all ingredients are currently available.")
                                    continue

            break


            
                

if __name__ == "__main__":
    welcome()
