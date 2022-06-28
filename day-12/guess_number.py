import random
from art import logo

print(logo)

HARD_LEVEL = 5
EASY_LEVEL = 10
ATTEMPTS = 0
SHOULD_PLAY = True

random_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
# print(f"Pssst, the correct answer is {random_number}")
chosen_level = input("Choose a difficulty. Type 'easy' or 'hard': hard ")

if chosen_level == "easy":
  attempts = EASY_LEVEL
elif chosen_level == "hard":
  attempts = HARD_LEVEL
else:
  print("Invalid input")
  SHOULD_PLAY = False

def number_guess():
  global ATTEMPTS
  global random_number
  global SHOULD_PLAY
  guess = int(input(f"Make a guess: "))
  if guess > random_number:
    print("Too high!")
    ATTEMPTS -= 1
  elif guess < random_number:
    print("Too low!")
    ATTEMPTS -= 1
  else:
    print(f"You got it! The answer was {random_number}.")
    SHOULD_PLAY = False

while SHOULD_PLAY:
  if ATTEMPTS == 0:
    should_play = False
    print(f"You've run out of guesses, you lose.")
  else:
    print(f"You have {ATTEMPTS} attempts remaining to guess the number.")
    number_guess()