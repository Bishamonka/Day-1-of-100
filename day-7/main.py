# Import Modules
import random
import hangman_art
import hangman_words
from replit import clear

chosen_word = random.choice(hangman_words.word_list) # Get Random Word
word_length = len(chosen_word)

print(hangman_art.logo) # Game Logo

display = ["_"] * word_length

lives = 6
end_of_game = False
while not end_of_game:
    guess = input("\nGuess a letter: ").lower()

    clear() # Clears screen after guessing the new letter

    if guess in display:
        print(f"You've already guessed '{guess}'.\n")
        
    # Check guessed letter and 'writes' it True.
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(f"Letter '{guess}' is right!\n")

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"The '{guess}' is not the right letter. You loose life.\n")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose!\nThe word was '{chosen_word}'.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Win Condition
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])