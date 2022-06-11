# Preparations
rock = '''

ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''

PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors = '''

SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

import random
tool = [rock, paper, scissors]

# START
print("Welcome to the 'Rock, Paper, Scissors'!")
player_choice = int(input("What do you choose? Type '0' for Rock, '1' for Paper or '2' for Scissors. \n\nYour choice: "))
computer_choice = random.randint(0, 2)

# Here we CHECK if player typed correct number. If not, then we abort the game. (So no future errors with ranges and images.)
if (player_choice < 3):
  
  # Visualisation
  print(f"\nYou played with: {tool[player_choice]}")
  print(f"Computer played with: {tool[computer_choice]}")
  
  # Here goes the whole logic. Reminder:
  # 0 - Rock
  # 1 - Paper
  # 2 - Scissors
  
  # IF for all WINS CONDITIONS
  # ELIF for DRAW
  # ELSE for all LOOSE CONDITIONS 
  
  if (tool[player_choice] == 0 and tool[computer_choice] == 2) or (tool[player_choice] == 1 and tool[computer_choice] == 0) or (tool[player_choice] == 2 and tool[computer_choice] == 1):
    print("You win!")
  elif (tool[player_choice] == tool[computer_choice]):
    print("It's a draw.")
  else:
    print("You loose.")
else:
  exit(print("You typed invalid number. Please restart the game."))
