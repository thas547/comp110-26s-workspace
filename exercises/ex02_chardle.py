"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730733868"


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
        """I accidentally put the return statement on the same line as exit and wasnt sure why it didnt work for a bit"""
    return word


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    """I wasn't completely sure about the count or index or where to put them, the number of equals signs on each was also kind of confusing"""
    count: int = 0
    if word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1
        """all the if statements got pretty tedious"""
    if count == 0:
        print("No instances of " + letter + " found in " + word)
        """I know theres probably a more efficient way of doing these final two but i didnt know how to do it"""
    else:
        if count == 1:
            print("1 instance of " + letter + " found in " + word)
        else:
            print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
