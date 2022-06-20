# Import stuff
from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

# Print visual
print(logo
     )
all_bids = {}
should_continue = True
while should_continue:
  name = input("What's your name? ")
  bid = int(input("What's your bid? $"))
  all_bids[name] = bid
  ask_to_continue = input("Are there other users who wants to bid? ('yes' to contine, 'no' to reveal the winner)").lower()
  if ask_to_continue == "no":
    should_continue = False
  elif ask_to_continue == "yes":
    clear()
  else:
    print("Invalid input.")
    
# Gotta find the winner
winner_bid = {}
top_bid = 0

for name in all_bids:
  if all_bids[name] > top_bid:
    top_bid = all_bids[name]
    winner_bid = {}
    winner_bid[name] = all_bids[name]
for name in winner_bid:
  winner_name = name
print(winner_bid)    
print(f"The winner is {winner_name} who bet ${winner_bid[name]}!")   
