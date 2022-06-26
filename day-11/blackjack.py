def blackjack():
  
  import random
  from art import logo

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

  #
    
  game_continues = True
  while game_continues:
    
    player_hand.extend(first_two_cards())
    dealer_hand.extend(first_two_cards())

    # Player's Turn
    player_turn = True
    while player_turn:

      print("Metadata: PY-Blackjack v.0.1.0 \n")
      print(logo)
      
      player_score = 0
      player_score = score_points(player_hand, player_score)
      
      print(f"Your cards: {player_hand}, current score: {player_score}")
      print(f"Computer's first card: {dealer_hand[0]}")

      if player_hand == [11, 10] or player_hand == [10, 11]:
        print(f"\n{player_hand[0]} and {player_hand[1]} from start! it's a BLACKJACK! You win! 😃")
        player_turn = False
        game_continues = False
      
      if player_score > 21:
        player_turn = False
    
      if player_score < 22:
        should_play = input(f"\nType 'y' to get another card, type 'n' to pass: ").lower()
        if should_play == "y":
          player_hand.append(random_card())
        else:
          player_turn = False

      clear()
    
    # Dealer Taking Cards
    dealer_turn = True
    while dealer_turn:
      dealer_score = 0
      dealer_score = score_points(dealer_hand, dealer_score)
      if dealer_score < 17:
        dealer_hand.append(random_card())
        if dealer_score > 21 and 11 in dealer_hand:
          dealer_hand[dealer_hand.index(11)] = 1
      else:
        dealer_turn = False

    print("Metadata: PY-Blackjack v.0.1.0 \n")
    print(logo)
    
    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    
    if player_score > 21:
      print("You went over 21. You loose 😭")
    elif player_score == dealer_score:
      print("\nIt's a Draw... 😤")  
    elif player_score <= 21 and dealer_score < player_score:
      print("\nYou win! 😃")
    elif dealer_score <= 21 and player_score < dealer_score:
      print("\nYou loose 😭")
    elif player_score <= 21 and dealer_score > 21:
      print("\nDealer went over 21. You win! 😃")
    game_continues = False

  print(f"SCORE: Dealer {dealer_wins} * You {player_wins}")
  play_again = input(f"\nDo you want to play again? Type 'y' or 'n': ")
  if play_again == "y":
    clear()
    blackjack()

from replit import clear
play = input(f"Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play == "y":
  clear()
  blackjack()
