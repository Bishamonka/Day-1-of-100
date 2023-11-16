print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride")
  age = int(input("What is your age? "))
  bill = 0

  if age >= 45 and age <= 55:
    print("It's free for you!")
  elif age < 12:
    print("Child tickets are $5")
    bill += 5
  elif age < 18:
    print("Youth tickets are $7")
    bill += 7
  elif age >= 18:
    print("Adult tickets are $12")
    bill += 12

  wants_photo = input("Do you want photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  print(f"Your total bill is: ${bill}")
else:
  print("Go away midget!")