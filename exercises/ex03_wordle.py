"""ex03"""

__author__ = "730733868"

WHITE_BOX: str = "\U00002b1c"
GREEN_BOX: str = "\U0001f7e9"
YELLOW_BOX: str = "\U0001f7e8"


def input_guess(length_word: int) -> str:
    guess: str = input(f"Enter a {length_word} character word: ")
    while len(guess) != length_word:
        print(f"That wasn't {length_word} chars! Try Again: ")
        guess: str = input(f"Enter a {length_word} character word: ")
    return guess


"""looking for specific letter, like a normal wordle, and returning true if there is a match and false if not"""

"""I mixed up the less than sign with less than or equal and was confused why I was seeing an error"""


def contains_char(secret_word: str, char_guess: str) -> bool:
    assert len(char_guess) == 1
    index: int = 0
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        index += 1
    return False


"""It took me a bit to understand the emojies, also the three different cases threw me off"""


def emojified(guess: str, secret: str) -> str:
    """"""
    assert len(guess) == len(secret)
    index: int = 0
    emoji: str = ""
    while index < len(secret):
        if guess[index] == secret[index]:
            emoji += GREEN_BOX
        elif contains_char(secret_word=secret, char_guess=guess[index]):
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        index += 1
    return emoji


"""This was the hardest part for me I didnt get the won variable right away"""


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    count = 1
    won: bool = False
    while count < 7 and not won:
        print(f"=== Turn {count}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess=guess, secret=secret))
        if guess == secret:
            won = True
        else:
            won = False
            count += 1
    if won:
        print(f"You won in {count}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
