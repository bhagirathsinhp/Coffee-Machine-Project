from resources import resources, MENU

LATTE_COST = MENU['latte']['cost']
ESPRESSO_COST = MENU['espresso']['cost']
CAPPUCCINO_COST = MENU['cappuccino']['cost']

QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01

water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
money = 0

# Function to display the report of the available resources:
def display_resources(user_input):
    if user_input == "report":
        for items in resources:
            if resources[items] == 0:
                print("Need to refill empty resources.")

        print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: {money}")

# # Function to process inserted coins:
# def process_coins(coins, user_input):
#     if user_input == "quarter":
#         quarter = coins * QUARTER
#     elif user_input == "dime":
#         dime = coins * DIME
#     elif user_input == "nickel":
#         nickel = coins * NICKEL
#     elif user_input == "penny":
#         penny = coins * PENNY
#
#     return quarter, dime, nickel, penny

make_coffee = True

while make_coffee:
    userInput = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if userInput == "off":
        print("Turning the machine off!")
        make_coffee = False

    if userInput == "report":
        display_resources(userInput)
        make_coffee = False

    if userInput == "latte":
        quarters = int(input("How many quarters: "))
        dimes = int(input("How many dimes: "))
        nickels = int(input("How many nickels: "))
        pennies = int(input("How many pennies: "))

        quarter = QUARTER * quarters
        dime = DIME * dimes
        nickel = NICKEL * nickels
        penny = PENNY * pennies

        total = quarter + dime + nickel + penny
        round_total = round(total, 2)
        print(f"Total amount in coins received: ${round_total}")

        if round_total < LATTE_COST:
            print("Insufficient coins inserted.")
            print(f"Add ${LATTE_COST - round_total}")
        elif round_total > LATTE_COST:
            print("Extra coins inserted.")
            refund_amount = round(round_total - LATTE_COST, 2)
            print(f"Total ${refund_amount} refunded.")
            print(f"{userInput.upper()} READY!")

    elif userInput == "espresso":

        quarters = int(input("How many quarters: "))
        dimes = int(input("How many dimes: "))
        nickels = int(input("How many nickels: "))
        pennies = int(input("How many pennies: "))

        quarter = QUARTER * quarters
        dime = DIME * dimes
        nickel = NICKEL * nickels
        penny = PENNY * pennies

        total = quarter + dime + nickel + penny
        round_total = round(total, 2)
        print(f"Total amount in coins received: ${round_total}")

        if round_total < ESPRESSO_COST:
            print("Insufficient coins inserted.")
            print(f"Add ${ESPRESSO_COST - round_total}")
        elif round_total > ESPRESSO_COST:
            print("Extra coins inserted.")
            refund_amount = round(round_total - ESPRESSO_COST, 2)
            print(f"Total ${refund_amount} refunded.")
            print(f"{userInput.upper()} READY!")


    elif userInput == "cappuccino":
        quarters = int(input("How many quarters: "))
        dimes = int(input("How many dimes: "))
        nickels = int(input("How many nickels: "))
        pennies = int(input("How many pennies: "))

        quarter = QUARTER * quarters
        dime = DIME * dimes
        nickel = NICKEL * nickels
        penny = PENNY * pennies

        total = quarter + dime + nickel + penny
        round_total = round(total, 2)
        print(f"Total amount in coins received: ${round_total}")

        if round_total < CAPPUCCINO_COST:
            print("Insufficient coins inserted.")
            print(f"Add ${CAPPUCCINO_COST - round_total}")
        elif round_total > CAPPUCCINO_COST:
            print("Extra coins inserted.")
            refund_amount = round(round_total - CAPPUCCINO_COST, 2)
            print(f"Total ${refund_amount} refunded.")
            print(f"{userInput.upper()} READY!")