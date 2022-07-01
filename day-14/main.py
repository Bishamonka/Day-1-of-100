import random
from replit import clear
from art import logo, vs
from game_data import data

score = 0

# Begin game loop:
end_game = False
while not end_game:
  
  print(logo)

  if score > 0: # So the message and score will appear after every successfull answer
    print(f"Correct! Your score now is: {score}") 


  # indext_of_a = random.randint(0, len(data) - 1)
  # indext_of_b = random.randint(0, len(data) - 1)
  # if indext_of_b == indext_of_a:
  #   while indext_of_b == indext_of_a:
  #     indext_of_b = random.randint(0, len(data))
  # variant_a = data[indext_of_a]
  # variant_b = data[indext_of_b]

  
  # Create two variants: A and B
  variant_a = random.choice(data)
  variant_b = random.choice(data)
  while variant_a == variant_b:
    variant_b = random.choice(data)
  
  # A way for every next round to get previous B variant as new variant A
  if score == 0:
    variant_c = {}
  else:
    variant_a = variant_c
    
  # Print information regarding current round/turn
  print(f"Compare A: {variant_a['name']}, a {variant_a['description']} from {variant_a['country']}")
  print(vs)
  print(f"Against B: {variant_b['name']}, a {variant_b['description']} from {variant_b['country']}")

  # Get followers count for future comparison
  followers_of_a = variant_a['follower_count']
  followers_of_b = variant_b['follower_count']

  # Function that returns dictionary with more followers. So now computer knows the right answer :)
  def comparison(followers_count_of_a, followers_count_of_b):
    if followers_count_of_a > followers_count_of_b:
      return variant_a
    else:
      return variant_b

  # We store right answer in separate variable so to be able to compare it with users's answer later.
  right_answer = comparison(followers_of_a, followers_of_b)

  # Assign user's answer to corresponding variable
  answer = input(f"Who has more followers? \nType 'A' or 'B': ").lower()
  if answer == "a":
    answer = variant_a
  elif answer == "b":
    answer = variant_b
  else:
    answer = {}

  # Finale. Check if user is right and perform corresponding output.
  if answer == right_answer:
    score += 1
    variant_c = variant_b # Store variant B as variant C for the next round/turn
    clear()
  else:
    clear()
    print(logo)
    print(f"Incorrect. You loose.\nYour score was: {score}")
    end_game = True
