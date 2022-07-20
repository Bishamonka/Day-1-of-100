import time
from menu import MENU
from menu import resources
MONEY = 0


def ask_user_choice():
    return input(f"""
What would you like?

1. Espresso: ${MENU['espresso']['cost']}
2. Latte: ${MENU['latte']['cost']}
3. Cappuccino: ${MENU['cappuccino']['cost']}

Your choice: """).lower()


def print_report():
    print(f"""
Water: {resources['water']}ml
Milk: {resources['milk']}ml
Coffee: {resources['coffee']}g
Money: ${MONEY}
    """)


def switch_off_machine():
    exit("Machine stopped.")


user_input = ask_user_choice()
drink_choice = user_input
drink_cost = 0
drink_name = ""

if 'milk' in drink_choice:
    milk_needed = True
else:
    milk_needed = False
if user_input == "off":
    switch_off_machine()
elif user_input == "report":
    print_report()
elif user_input == "espresso" or user_input == "1":
    drink_name = "Espresso"
    drink_cost = MENU['espresso']['cost']
    drink_ingredients = MENU['espresso']['ingredients']
elif user_input == "latte" or user_input == "2":
    drink_name = "Latte"
    drink_cost = MENU['latte']['cost']
    drink_ingredients = MENU['latte']['ingredients']
elif user_input == "cappuccino" or user_input == "3":
    drink_name = "Cappuccino"
    drink_cost = MENU['cappuccino']['cost']
    drink_ingredients = MENU['cappuccino']['ingredients']
else:
    print('Invalid Input. Try again.')
    switch_off_machine()


def resources_check(machine_resource, there_is_milk):
    """
    Checks if there are enough resources in machine to make a chosen drink.
    :param machine_resource:
    :param there_is_milk:
    :return: True / False
    """
    if machine_resource['water'] >= drink_ingredients['water']:
        if machine_resource['coffee'] >= drink_ingredients['coffee']:
            return True
    elif there_is_milk:
        if machine_resource['milk'] >= drink_ingredients['milk']:
            return True
    else:
        return False


enough_resources = resources_check(resources, milk_needed)

print(f"\nYou chose '{drink_name}'")
print(f"Please, insert ${drink_cost}")


def user_purchase():
    purchase = 0
    quarters = 25 * int(input(f"How many quarters?\n$0.25 x "))
    purchase += float("{:.2f}".format(quarters / 100))
    if purchase >= drink_cost:
        return purchase
    print(f"\nYour balance: ${purchase:.2f}")
    dimes = 10 * int(input(f"How many dimes?\n$0.10 x "))
    purchase += (dimes / 100)
    if purchase >= drink_cost:
        return purchase
    print(f"\nYour balance: ${purchase:.2f}")
    nickles = 5 * int(input(f"How many nickles?\n$0.05 x "))
    purchase += (nickles / 100)
    if purchase >= drink_cost:
        return purchase
    print(f"\nYour balance: ${purchase:.2f}")
    pennies = 1 * int(input(f"How many pennies?\n$0.01 x"))
    purchase += (pennies / 100)
    if purchase >= drink_cost:
        return purchase
    purchase = (quarters + dimes + nickles + pennies) / 100
    return purchase


user_purchase = user_purchase()
money_inserted = user_purchase
print(f"\nMoney inserted: ${money_inserted}")

if money_inserted >= drink_cost:
    change = money_inserted - drink_cost
    if money_inserted > drink_cost:
        print(f"Here's your change: ${change}")
    print(f"Drink is cooking...")
    for click in range(3, 0, -1):
        print(f"{click}")
        time.sleep(0.7)
    print(f"Here is your ☕️ {drink_name}! Enjoy!")
else:
    print(f"Sorry that's not enough money. Money refunded.")
    print(f"Here's your refund: ${money_inserted}")
