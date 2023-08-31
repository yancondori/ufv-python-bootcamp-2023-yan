# Import necessary libraries/modules
from h_art import logo  # The logo for the hangman game.
import random  # Module to generate random choices.

# Importing word_list which contains a list of possible words for the game.
from h_words import word_list

# Randomly selects a word from the word_list.
chosen_word = random.choice(word_list)
word_length = len(chosen_word)  # Determines the length of the chosen word.

# Initialize game conditions
end_of_game = False
lives = 6

# Print the game's logo at the start.
print(logo)

# Create a display list filled with "_" placeholders for each letter in the chosen word.
display = ["_"] * word_length

# Main game loop; continues until the game ends (win or lose).
while not end_of_game:
    # Prompt user for a letter and convert it to lowercase.
    guess = input("Guess a letter: ").lower()

    # Check if the guessed letter was already guessed before.
    if guess in display:
        print(f"You've already guessed {guess}")

    # Iterate over the chosen word to see if the guessed letter exists in it.
    for position, letter in enumerate(chosen_word):
        if letter == guess:
            display[position] = letter

    # If guessed letter is not in the chosen_word, reduce lives.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:  # If no lives are left, game over.
            end_of_game = True
            print("You lose.")

    # Display the current status of guessed letters.
    print(f"{' '.join(display)}")

    # If there are no more "_" in display, user wins.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Display the current hangman stage (based on lives left).
    from h_art import stages
    print(stages[lives])
