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

QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01

# Function takes in user input and total amount inserted, and calculates if it matches the price
def calculate_money(total_amount, user_input):
    coffee_cost = MENU[user_input]["cost"]

    if total_amount == 0:
        print("Please insert some coins!")

    elif total_amount < coffee_cost:
        print("Insufficient coins inserted.")
        print("Amount refunded, please try again!")

    elif total_amount > coffee_cost:
        print("Extra coins inserted!")
        refund_amount = total_amount - coffee_cost
        print(f"Amount refunded: ${round(refund_amount, 2)}")
        return True

    else:
        print(f"Amount received: ${total_amount}")
        print(f"A cup of {user_input.upper()} on the way!")
        return True

# Function takes in current resources and subtracts the flavour resources:
def update_resources(user_input, machine_resource):

    for resource in machine_resource:
        if resource in MENU[user_input]['ingredients']:
            machine_resource[resource] -= MENU[user_input]['ingredients'][resource]
        else:
            machine_resource[resource] -= 0

    updated_resource = {
        'water': machine_resource['water'],
        'milk': machine_resource['milk'],
        'coffee': machine_resource['coffee']
    }

    return updated_resource

# Function that takes in current resources and checks if anything is empty:
def check_resource(user_input, available_resource):
    for resource in available_resource:
        if available_resource[resource] == 0:
            print(f"Sorry, there is not enough {resource}.")
            return True

        elif resource not in MENU[user_input]['ingredients']:
            return False

        elif available_resource[resource] < MENU[user_input]['ingredients'][resource]:
            print(f"Sorry, there is not enough {resource}.")
            return True

# Function to run the coffee machine:
def coffee_machine():
    keep_going = True
    money = 0
    current_resources = resources
    # print(current_resources)

    while keep_going:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_choice == "report":
            print("MACHINE REPORT:")
            for resource in current_resources:
                print(f"{resource.upper()}: {current_resources[resource]}")
            print(f"MONEY: ${money}")

        elif user_choice == "off":
            print("Shutting the machine down!")
            return

        else:
            no_resource = check_resource(user_choice, current_resources)
            if no_resource:
                keep_going = False

            else:
                quarter_coins = int(input("How many quarters: ")) * QUARTER
                dime_coins = int(input("How many dimes: ")) * DIME
                nickel_coins = int(input("How many nickels: ")) * NICKEL
                penny_coins = int(input("How many pennies: ")) * PENNY

                total = quarter_coins + dime_coins + nickel_coins + penny_coins
                rounded_total = round(total, 2)

                success = calculate_money(rounded_total, user_choice)

                if success is True:
                    coffee_cost = MENU[user_choice]['cost']
                    money += coffee_cost
                    current_resources = update_resources(user_choice, current_resources)

coffee_machine()