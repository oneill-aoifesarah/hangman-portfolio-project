"""
Randomize and import word list
"""
import random
from words import word_list_easy, word_list_medium, word_list_hard


def get_word(difficulty):
    """
    Get a random word based on the difficulty level
    """
    if difficulty == 'easy':
        return random.choice(word_list_easy).upper()
    elif difficulty == 'medium':
        return random.choice(word_list_medium).upper()
    elif difficulty == 'hard':
        return random.choice(word_list_hard).upper()
    else:
        raise ValueError("Invalid difficulty level")


def display_hangman(attempts):
    """
    Display the hangman in six stages based on the number of incorrect attempts
    """
    hangman_stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        """
           ------
           |    |
           |
           |
           |
           |
        """
    ]
    return hangman_stages[attempts]


def print_game_state(attempts, word_completion):
    """
    Print the current game state (hangman and word completion).
    """
    print(display_hangman(attempts))
    print("Current Word:", word_completion, "\n")


def play(word, player_name):
    """
    Main game-playing function.
    """
    word_completion = " ".join(["_" for _ in word])
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 6

    ready_to_play = input(
     f"Hello, {player_name}! Are you ready to play Hangman? (Y/N): "
    ).upper()

    if ready_to_play != "Y":
        print("Maybe next time. Goodbye!")
        return

    print(f"Great, {player_name}! Let's play Hangman!")
    print("Here are the rules:")
    print("1. You need to guess the hidden word.")
    print("2. You can guess a letter at a time or the entire word.")
    print("3. You have 6 attempts to guess the word correctly.")
