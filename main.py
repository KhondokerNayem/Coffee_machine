MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def coin_calculate():
    print("quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01")
    quarters = int(input("How many quarters? : "))
    dimes = int(input("How many dimes? : "))
    nickles = int(input("How many nickles? : "))
    pennies = int(input("How many pennies? : "))
    return quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01
def check_availability(user):
    global resources
    if user == "espresso":
        if MENU[user]["ingredients"]["water"]<=resources["water"] and MENU[user]["ingredients"]["coffee"]<=resources["coffee"]:
            return True
        else :
            if MENU[user]["ingredients"]["water"] > resources["water"]:
                print(f"Not enough water for {user}!")
            if MENU[user]["ingredients"]["coffee"] >resources["coffee"]:
                print(f"Not enough coffee for {user}!")
            return False
    elif user == "latte":
        if MENU[user]["ingredients"]["water"] <= resources["water"] and MENU[user]["ingredients"]["coffee"] <= resources[
            "coffee"] and MENU[user]["ingredients"]["milk"] <= resources["milk"]:
            return True
        else:
            if MENU[user]["ingredients"]["water"] > resources["water"]:
                print(f"Not enough water for {user}!")
            if MENU[user]["ingredients"]["coffee"] > resources["coffee"]:
                print(f"Not enough coffee for {user}!")
            if MENU[user]["ingredients"]["milk"] >resources["milk"]:
                print(f"Not enough milk for {user}!")
            return False
    elif user == "cappuccino":
        if MENU[user]["ingredients"]["water"] <= resources["water"] and MENU[user]["ingredients"]["coffee"] <= resources[
            "coffee"] and MENU[user]["ingredients"]["milk"] <= resources["milk"]:
            return True
        else:
            if MENU[user]["ingredients"]["water"] > resources["water"]:
                print(f"Not enough water for {user}!")
            if MENU[user]["ingredients"]["coffee"] > resources["coffee"]:
                print(f"Not enough coffee for {user}!")
            if MENU[user]["ingredients"]["milk"] >resources["milk"]:
                print(f"Not enough milk for {user}!")
            return False
total_money = 0
money = 0
run = True
# print(f"Total : {total_money}")
while run:
    user = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user == "report":
        print(f"Here is the report:\nWater : {resources["water"]} ml\nmilk : {resources["milk"]} ml\ncoffee : {resources["coffee"]} mg\nmoney : ${total_money}")
    elif user == "off":
        print("Machine is now off!")
        break
    elif user == "espresso":
        # print("Please insert coins.")
        if check_availability(user):
            money = coin_calculate()
            if money>MENU[user]["cost"]:
                resources["water"] -= MENU[user]["ingredients"]["water"]
                resources["coffee"] -= MENU[user]["ingredients"]["coffee"]
                print(f"Here is your change : ${money-MENU[user]["cost"]}")
                print(f"Enjoy your {user}!")
                total_money +=MENU[user]["cost"]
                # print(f"profit : {total_money}")
            else:
                print("You do not entered enough money!")



    elif user == "latte":
        # print("Please insert coins.")
        if check_availability(user):
            money = coin_calculate()
            if money > MENU[user]["cost"]:
                resources["water"] -= MENU[user]["ingredients"]["water"]
                resources["coffee"] -= MENU[user]["ingredients"]["coffee"]
                resources["milk"] -= MENU[user]["ingredients"]["milk"]
                print(f"Here is your change : ${money - MENU[user]["cost"]}")
                print(f"Enjoy your {user}")
                total_money += MENU[user]["cost"]
                # print(f"profit : {total_money}")
            else:
                print("You do not entered enough money!")


    elif user == "cappuccino":
        # print("Please insert coins.")
        if check_availability(user):
            money = coin_calculate()
            if money > MENU[user]["cost"]:
                resources["water"] -= MENU[user]["ingredients"]["water"]
                resources["coffee"] -= MENU[user]["ingredients"]["coffee"]
                resources["milk"] -= MENU[user]["ingredients"]["milk"]
                print(f"Here is your change : ${money - MENU[user]["cost"]}")
                print(f"Enjoy your {user}")
                total_money += MENU[user]["cost"]
                # print(f"profit : {total_money}")
            else:
                print("You do not entered enough money!")
print(f"Total profit : ${total_money}")