import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Display the current snowman stage, word progress
    and guessed letters.
    """
    print(STAGES[mistakes])

    display_word = "".join(
        [letter if letter in guessed_letters else "_" for letter in secret_word]
    )
    print("Word: " + display_word)
    print("Mistakes: " + str(mistakes))
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print()


def get_random_word():
    """Return a random secret word from the word list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    """
    Run a single round of the Snowman Meltdown game.
    """
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter only one letter!")
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

def main():
    """
    Start the game loop and ask the player if they want to replay.
    """
    while True:
        play_game()
        again = input("\nWould you like to play again? (j/n): ").lower()
        if again != "j":
            print("Thanks for playing!")
            break