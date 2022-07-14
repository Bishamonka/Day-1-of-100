print("Hello word!")
print("Finally! We are moving to Py Charm. I can`t wait to start building stuff in here!")
print("I've missed yesteeday's contribution... This is gonna drive me crazy for a whole year( ")
print("2 Days")
print("More than that...")
print("It was tough week")
print("A terrible headache...")
print("I slept for the whole evening. It's ruined. It's 23:30 now.")
print("Missing just one day kicked my wish to do anything right to the floor. But seems like I really like it so'll continue... step by step, baby step.")

MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
    }
}

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
}

money = 0


def ask_user_choice():
    return input(f"""
What would you like?

Espresso: ${MENU['espresso']['cost']}
Latte: ${MENU['latte']['cost']}
Cappuccino: ${MENU['cappuccino']['cost']}

Your choice: """).lower()


def report():
    print(f"""
Water: {resources['water']}ml
Milk: {resources['milk']}ml
Coffee: {resources['coffee']}g
Money: ${money}
    """)


def switch_off():
    exit("Machine stopped")


user_input = ask_user_choice()
if user_input == "off":
    switch_off()
elif user_input == "report":
    report()
elif user_input == "espresso":
    print(f"User wants Espresso")
elif user_input == "latte":
    print(f"User wants Latte")
elif user_input == "cappuccino":
    print(f"User wants Cappuccino")


