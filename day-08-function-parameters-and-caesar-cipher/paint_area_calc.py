import math

def paint_calc(height, width, cover):
    num_cans = (height * width) / cover
    round_up_cans = math.ceil(num_cans)
    print(f"You'll need {round_up_cans} cans of paint.")

h = int(input("Height of wall: "))
w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=h, width=w, cover=coverage)
