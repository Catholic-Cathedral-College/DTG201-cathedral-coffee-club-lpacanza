#Main Coffee Bot function
orders = []
def coffee_bot():
    welcome_message()
    order_taking(orders)
    receipt(orders)

    name = input("\nCan I get your name please? ")

    print("\nThanks, {}! Please proceed to the pick up counter for your order!".format(name))

#Welcome Message, called in main function
def welcome_message():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nWelcome to the Cathedral Coffee Club!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nToday's specials are Caramel Macchiato and Cherry Spice Cold Brew.\n Here's our menu!:")
    print("+------------------------------------------+")
    print("|¸.··.¸¸.··.¸¸.·♩♪♫ Menu ♫♪♩·.¸¸.··.¸¸.··.¸|")
    print("+----------------------------+-------------+")
    print("|          Coffee            |    Price    |")
    print("+----------------------------+-------------+")
    print("|        Flat White          |    $3.00    |")
    print("|        Cappuccino          |    $3.00    |")
    print("|          Latte             |    $3.50    |")
    print("|          Decaf             |    $3.00    |")
    print("|      Hot Chocolate         |    $4.00    |")
    print("+----------------------------+-------------+")
  
#Order Taking, called in main function
def order_taking(orders):
    size = get_size()
    temp_type = get_temp()
    drink_type = get_drink_type()
    cup_type = get_cup()
    quantity = get_quantity()
    orders.append([quantity, size, temp_type, drink_type, cup_type])
    print("\n" + str(orders))
    print("\nAlright, that\'s {} {} {} {} {}!".format(quantity, size, temp_type, drink_type, cup_type))
    addon_prompt()

#For Additional Orders, called in Order Taking function
def addon_prompt():
    res = input("\nDo you wish to add another order? \n[a] Yes \n[b] No \n> ")
    res = res.lower()
    if res == "a":
        print("\nAlright, taking your new order!")
        return order_taking(orders)
    else:
        print("\nAlright, processing your orders now!")

#Error Message, used for invalid input
def error_message():
    print("\nI'm sorry, I did not understand your selection.\n\nPlease enter the corresponding letter for your response.")

#Order Summary, called in main function
def receipt(orders):
    total_orders = range(1, (len(orders)+1))
    print("\n┏-------------------Receipt-------------------┓\n\nYou have placed " + str((len(orders))) + " order(s). Your orders are: \n\n┣---------------------------------------------┫\n")
    for order in orders:
        print(*order)
        print("\n┗---------------------------------------------┛\n")

#Size Choice, called in Order Taking function
def get_size():
    res = input('\nWhat size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
    res = res.lower()
    if res == "a":
        return "Small"
    elif res == "b":
        return "Medium"
    elif res == "c":
        return "Large"
    else:
        error_message()
        return get_size()

#Drink Choice, called in Order Taking function
def get_drink_type():
    res = input("\nWhat type of drink would you like?\n[a] Flat White \n[b] Cappuccino \n[c] Latte \n[d] Decaf \n[e] Hot Chocolate \n> ")
    res = res.lower()
    if res == "a":
        return "Flat White"
    elif res == "b":
        return "Cappuccino"
    elif res == "c":
        return order_latte()
    elif res == "d":
      return "Decaf"
    elif res == "e":
      return "Hot Chocolate"
    else:
        error_message()
        return get_drink_type()

#Milk Component, called in Get_Drink_Type function
def order_latte():
    res = input("\nAnd what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ")
    res = res.lower()
    if res == "a":
        return "Latte"
    elif res == "b":
        return "Non-fat Latte"
    elif res == "c":
        return "Soy Latte"
    else:
        error_message()
        return order_latte()

#Temp Choice, called in Order Taking function
def get_temp():
    res = input("\nHow would you like your drink? \n[a] Hot \n[b] Iced \n> ")
    res = res.lower()
    if res == "a":
        return "Hot"
    elif res == "b":
        return "Iced"
    else:
        error_message()
        return get_temp()

#Cup choice, called in Order Taking function
def get_cup():
    res = input("\nWhat type of cup would you like to use?\n[a] Dine-in Cup \n[b] Takeaway Cup \n[c] Your own Reusable Cup \n> ")
    res = res.lower()
    if res == "a":
        return "in a dine-in cup"
    elif res == "b":
        return "in a takeaway cup."
    elif res == "c":
        return "in your reusable cup."
    else:
        error_message()
        return get_cup()

#Quantity choice, called in Order Taking function
def get_quantity():
    res = input("\nWhat is quantity for this order? > ")
    try:
        res = int(res)
        return res
    except ValueError:
        print("\nInvalid input. Please enter a value quantity.")
        return get_quantity()

coffee_bot()
