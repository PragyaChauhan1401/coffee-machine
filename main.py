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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("please insert coins")
    total = int(input("how many quaters? :"))*0.25
    total += int(input("how many dimes  ? :")) * 0.10
    total += int(input("how many nikels? :")) * 0.05
    total += int(input("how many pennies? :")) * 0.01
    return total

def catchup_resources(drink_ingredient):
    for item in drink_ingredient:
        resources[item] -= drink_ingredient[item]



is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report' :
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[choice]
        if is_sufficient(drink['ingredients']):
            total = process_coins()
            if total >= drink['cost']:
                change = round(total - drink['cost'] , 2)
                profit += drink['cost']
                print(f"Here is your change ${change} ")
                print("enjoy your coffee")
                catchup_resources(drink["ingredients"])
            elif total < drink['cost']:
                print("Sorry that's not enough money. Money refunded.")

