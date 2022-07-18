from menu import MENU
from menu import resources
MONEY = 0


def ask_user_choice():
    return input(f"""
What would you like?

Espresso: ${MENU['espresso']['cost']}
Latte: ${MENU['latte']['cost']}
Cappuccino: ${MENU['cappuccino']['cost']}

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

if 'milk' in drink_choice:
    milk_needed = True
else:
    milk_needed = False


if user_input == "off":
    switch_off_machine()
elif user_input == "report":
    print_report()
elif user_input == "espresso":
    drink_cost = MENU['espresso']['cost']
    drink_ingredients = MENU['espresso']['ingredients']
elif user_input == "latte":
    drink_cost = MENU['latte']['cost']
    drink_ingredients = MENU['latte']['ingredients']
elif user_input == "cappuccino":
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


def user_purchase():
    print("Please, insert money:")
    quarters = 0.25 * int(input(f"How many quarters?\n"))
    dimes = 0.10 * int(input(f"How many dimes?\n"))
    nickles = 0.05 * int(input(f"How many nickles?\n"))
    pennies = 0.01 * int(input(f"How many pennies?\n"))
    purchase = quarters + dimes + nickles + pennies
    global MONEY
    MONEY += purchase
    return purchase


print(f"User chose: {drink_choice}")
print(f"Drink costs: {drink_cost}")
print(f"Ingredients: {drink_ingredients}")
print(f"Machine has enough resources: {enough_resources}")
user_purchase = user_purchase()
money_inserted = user_purchase
print(f"Last purchase: {money_inserted}")


if money_inserted >= drink_cost:
    change = money_inserted - drink_cost
    print(f"Success! Enjoy your coffee!")
    print(f"Here's your change: ${change}")
else:
    print(f"Sorry that's not enough money. Money refunded.")
    print(f"Here's your refund: ${money_inserted}")
