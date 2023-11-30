"""
Randomize and import word list
"""
import random
from words import word_list_easy, word_list_medium, word_list_hard


def get_word(difficulty):
    """
    Get a random word based on the difficulty level.
    """
    if difficulty == 'easy':
        return random.choice(word_list_easy).upper()
    elif difficulty == 'medium':
        return random.choice(word_list_medium).upper()
    elif difficulty == 'hard':
        return random.choice(word_list_hard).upper()
