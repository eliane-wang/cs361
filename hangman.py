import random
import time


# Load words from a file and return as a list.
def load_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words
    

# Display game instructions to the user.
def display_instructions():
    instructions = """
    Welcome to Hangman!
    The goal of the game is to guess the word one letter at a time.
    If you guess a correct letter, it will be revealed in the word.
    If you guess an incorrect letter, you lose a life.
    You have 6 lives. Good luck!
    Benefits: By understanding the game rules, you can improve your gameplay and enjoy the game more.
    """
    start_time = time.time()
    print(instructions)
    end_time = time.time()
    # Check that the instructions are displayed quickly.
    assert end_time - start_time < 1, "Instructions took too long to display"


# Choose a random word from the list of words.
def choose_word(words):
    return random.choice(words)


# Display the main menu and return the chosen word for a new game.
def initialize_game(words):
    print("Welcome to Hangman!")
    while True:
        choice = input("Enter '1' to view instructions, '2' to start a new game, or '3' to quit: ")
        if choice == '1':
            display_instructions()
        elif choice == '2':
            return choose_word(words)
        elif choice == '3':
            print("Thank you for playing! Goodbye!")
            exit()
        else:
            print("Invalid input. Please enter '1', '2', or '3'.")


# Play a game of Hangman with the given word.
def play_game(word, words):
    word_display = ['_'] * len(word)  # Display word with blanks for unknown letters.
    guessed_letters = []  # Track guessed letters.
    lives = 6  # Number of lives the player starts with.
    last_guess_time = 0  # Track the time of the last guess to enforce wait time.

    while lives > 0 and '_' in word_display:
        # Display current game state.
        print(f"Word: {' '.join(word_display)}")
        print(f"Lives: {lives}")
        print(f"Guessed Letters: {', '.join(guessed_letters)}")

        guess = input("Guess a letter or type 'menu' to return to the main menu: ").lower()
        
        if guess == 'menu':
            # Ask for confirmation to return to the main menu.
            confirm = input("Are you sure you want to return to the main menu? (yes/no): ").lower()
            if confirm == 'yes':
                return None  # Return to the main menu
            else:
                continue
        
        current_time = time.time()
        if current_time - last_guess_time < 0.5:
            # Check if the user is making guesses too quickly.
            print("Please wait before making another guess.")
            continue
        last_guess_time = current_time
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        guessed_letters.append(guess)
        
        if guess in word:
            # Update the display with correctly guessed letters.
            for i, letter in enumerate(word):
                if letter == guess:
                    word_display[i] = guess
        else:
            # Reduce the number of lives for incorrect guesses.
            lives -= 1
            print("Incorrect guess. You lose a life. Cost: Losing a life decreases your chances to guess the word.")

        print(display_hangman(lives))

    # Determine the outcome of the game.
    if '_' not in word_display:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

    while True:
        # Ask if the user wants to play again.
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'yes':
            return choose_word(words)
        elif play_again == 'no':
            return None  # Return to the main menu
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


# Display the hangman visual based on the number of tries left.
def display_hangman(tries):
    stages = [  # Final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # Head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # Head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # Head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # Head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # Head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # Initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


# Main function to run the game.
def main():
    words = load_words('words.txt')
    while True:
        word = initialize_game(words)
        while word:
            word = play_game(word, words)

if __name__ == "__main__":
    main()
