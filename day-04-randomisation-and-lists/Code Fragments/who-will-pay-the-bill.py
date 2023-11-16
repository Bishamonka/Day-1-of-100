import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

offset_index = len(names)
print(f"{names[random.randint(0, offset_index - 1)]} is going to buy the meal today!")