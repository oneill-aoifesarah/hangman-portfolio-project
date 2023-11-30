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
