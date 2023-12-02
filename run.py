"""
Import from words.py
"""
import random
from words import word_list_easy, word_list_medium, word_list_hard


def get_word(difficulty):
    """
    Get a random word based on the difficulty level.
    This function takes a difficulty level and returns
    a randomly selected word corresponding to that difficulty level.
    If the difficulty level is not valid, it raises a ValueError.
    """
    difficulty = difficulty.lower()
    if difficulty == 'easy':
        return random.choice(word_list_easy).upper()
    elif difficulty == 'medium':
        return random.choice(word_list_medium).upper()
    elif difficulty == 'hard':
        return random.choice(word_list_hard).upper()
    else:
        raise ValueError("Invalid entry. Try again")


def display_hangman(attempts):
    """
    Display the hangman in six stages based on the number of attempts.
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


def handle_letter_guess(
    guess, word, word_completion, guessed_letters, attempts
):
    """
    Handle a letter guess. Add input validation.
    """
    if not guess.isalpha():
        print("Invalid input. Please enter a valid letter.")
        return word_completion, attempts

    guess = guess.upper()

    if guess in guessed_letters:
        print("You already tried the letter", guess)
    elif guess not in word:
        print(guess, "isn't in the word.")
        attempts -= 1
        guessed_letters.append(guess)
    else:
        print("Well done! The letter", guess, "is in the word!")
        guessed_letters.append(guess)
        word_completion = update_word_completion(guess, word, word_completion)

    return word_completion, attempts


def update_word_completion(guess, word, word_completion):
    """
    Update the word completion based on a correct letter guess.
    """
    word_as_list = list(word_completion.replace(" ", ""))
    indices = [i for i, letter in enumerate(word) if letter == guess]
    for index in indices:
        word_as_list[index] = guess
    updated_completion = " ".join(word_as_list)

    for i, char in enumerate(word_completion):
        if char.isspace():
            updated_completion = (
                updated_completion[:i] +
                char +
                updated_completion[i + 1:]
            )

    return updated_completion


def handle_word_guess(guess, word, guessed_words, attempts):
    """
    Handle a word guess. Add input validation.
    """
    if not guess.isalpha():
        print("Invalid input. Please enter a valid word.")
        return attempts

    guess = guess.upper()

    if guess in guessed_words:
        print("You already tried the word", guess)
    elif guess != word:
        print("Sorry, the word is not", guess + ".")
        attempts -= 1
        guessed_words.append(guess)
    else:
        print("Congratulations! You guessed the word correctly!")

    return attempts


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
        print("Maybe next time.")
        return

    print(f"Great, {player_name}! Let's play Hangman!")
    print("Here are the rules:")
    print("1. You need to guess the hidden word.")
    print("2. You can guess a letter at a time or the entire word.")
    print("3. You have 6 attempts to guess the word correctly.")

    while not guessed and attempts > 0:
        print_game_state(attempts, word_completion)
        guess = input("Please guess a letter or the entire word: ").upper()

        if len(guess) == 1 and guess.isalpha():
            word_completion, attempts = handle_letter_guess(
                guess, word, word_completion, guessed_letters, attempts
            )
        elif len(guess) == len(word) and guess.isalpha():
            attempts = handle_word_guess(guess, word, guessed_words, attempts)
            guessed = True
        else:
            print("Invalid input. Please enter a valid letter or word.")

    if guessed:
        print(f"The word is: {word}")
    else:
        print_game_state(attempts, word_completion)
        print(f"Sorry, {player_name}, no attempts left. The word was {word}.")


def main():
    """
    Main function to start the game, including loop for multiple games.
    """
    while True:
        player_name = input("Enter your name: ")
        difficulty = input("Choose difficulty (easy, medium, hard): ").lower()

        try:
            word = get_word(difficulty)
        except ValueError as e:
            print(e)
            continue

        play(word, player_name)

        play_again = input("Do you want to play again? (Y/N): ").lower()
        if play_again != 'y':
            print(f"Thanks for playing, {player_name}! Goodbye!")
            break


"""
Call main function when script is running
"""
if __name__ == "__main__":
    main()
