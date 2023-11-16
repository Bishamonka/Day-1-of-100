import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

machine_works = True

while machine_works:
    choice = input(f"What would you like? ({menu.get_items()})\n").lower()
    if choice == "off":
        machine_is_running = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        if menu.find_drink(choice):  # Checks if user chose position that exists in 'Menu'
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
