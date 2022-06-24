############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##########################################
def blackjack():
  # Imports
  import random
  from art import logo
  
  # Intro and welcome statement:
  
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  
  player_hand = []
  player_score = 0
  
  dealer_hand = []
  dealer_score = 0
  
  # FUNCTION: Create any players hands by givving them first two cards (creating a list):
  def first_two_cards():
    return random.sample(cards, 2)
  
  # FUNCTION: Random Card
  def random_card():
    return random.choice(cards)
  
  # FUNCTION: Calculate Score Points 
  def score_points(hand, score):
    for cards in hand:
      score += cards
      if score > 21 and 11 in hand:
          hand[hand.index(11)] = 1
    return score
    
  # FUNCTION: Show Current Game Status/Information
  def current_status():
    print(f"Your cards: {player_hand}, current score: {player_score}")
    print(f"Computer's first card: {dealer_hand[0]}")
  
  # GAME >>>
    
  game_continues = True
  while game_continues:
    
    # Give Cards to players
    player_hand.extend(first_two_cards())
    dealer_hand.extend(first_two_cards())

    if 10 in player_hand and 11 in player_hand:
      print(f"\n{player_hand[0]} and {player_hand[1]} from start! it's a BLACKJACK! You win! 😃")
      game_continues = False
    
    player_turn = True
    while player_turn:

      print("Metadata: PY-Blackjack v.0.1.0 \n")
      print(logo)
      
      player_score = 0
      player_score = score_points(player_hand, player_score)
      
      print(f"Your cards: {player_hand}, current score: {player_score}")
      print(f"Computer's first card: {dealer_hand[0]}")
      
      if player_score > 21:
        player_turn = False
    
      if player_score < 22:
        should_play = input(f"\nType 'y' to get another card, type 'n' to pass: ").lower()
        if should_play == "y":
          player_hand.append(random_card())
        else:
          player_turn = False

      clear()
    
    
    # Your final hand: [10, 5, 10], final score: 25
    # Computer's final hand: [8, 6, 7], final score: 21
    # You went over. You lose 😭
    
    # Dealer Taking Cards
    dealer_turn = True
    while dealer_turn:
      dealer_score = 0
      dealer_score = score_points(dealer_hand, dealer_score)
      if dealer_score < 17:
        dealer_hand.append(random_card())
      else:
        dealer_turn = False

    print("Metadata: PY-Blackjack v.0.1.0 \n")
    print(logo)
    
    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    
    if player_score > 21:
      print("You went over 21. You loose 😭")
    elif player_score == dealer_score:
      print("\nIt's a Draw...")
    elif player_score <= 21 and dealer_score < player_score:
      print("\nYou win! 😃")
    elif dealer_score <= 21 and player_score < dealer_score:
      print("\nYou loose 😭")
    elif player_score <= 21 and dealer_score > 21:
      print("\nDealer went over 21. You win! 😃")
    game_continues = False
    
  play_again = input(f"\nDo you want to play again? Type 'y' or 'n': ")
  if play_again == "y":
    clear()
    blackjack()

from replit import clear
play = input(f"Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play == "y":
  clear()
  blackjack()