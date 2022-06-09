#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇


print("Welcome to the tip calculator!")
bill = input("What was the total bill? \n$")
tip = input("How much tip would you like to give? (Usually: 10%, 12%, or 15%) \n%")
people = input("How many people to split the bill? \n")
result = round((float(bill) / int(people) * (float(tip)/100 + 1)), 2)
result = "{:.2f}" .format(result)
message = f"Each person should pay: ${result}"

print(message)