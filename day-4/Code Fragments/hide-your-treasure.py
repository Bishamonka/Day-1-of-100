row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to hide the treasure? \nWrite coodinates using two digit number (xy), 'x' for columns and 'y' for rows. (f.e. 11, 23, 31)\nYour coordinates are: ")

x = int(position[1]) - 1
y = int(position[0]) - 1

map[x][y] = "🟥"

print(f"{row1}\n{row2}\n{row3}")