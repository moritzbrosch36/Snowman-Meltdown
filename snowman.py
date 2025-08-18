import random

# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the mistakes"""
    print(STAGES[mistakes])

    display_word = "".join([letter if letter in guessed_letters else "_"
                            for letter in secret_word])
    print("Word: " + display_word)
    print("Mistakes: " + str(mistakes))
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print()


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        # TODO: Build your game loop here.
        # For now, simply prompt the user once:
        guess = input("Guess a letter: ").lower()

        print("Secret word selected: " + secret_word)  # for testing, later remove this line

        if not guess.isalpha() or len(guess) != 1:
            print("Please only letters!")
            continue

        if guess in guessed_letters:
            print("You've already guessed the letter!")
            continue

        guessed_letters.add(guess)

        if guess not in secret_word:
            mistakes += 1


        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("You win! The word was:", secret_word)
            return

        print("You guessed:", guess)

    display_game_state(mistakes, secret_word, guessed_letters)
    print("You lost! The word was:", secret_word)

if __name__ == "__main__":
    play_game()