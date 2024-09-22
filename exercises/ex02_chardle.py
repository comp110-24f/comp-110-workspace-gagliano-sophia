"""EX02 - Chardle: A new version of Wordle."""

__author__ = "730699412"


def input_word() -> str:
    """Takes input for a five character word and checks if it is five characters."""
    word: str = input("Enter a 5-character word:")
    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        # code should exit after the error message but before returning
        return word


def input_letter() -> str:
    """Takes input for a single character and checks if it is a single character."""
    letter: str = input("Enter a single character:")
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()
        return letter


def contains_char(word: str, letter: str) -> None:
    """Prints where the letter is found in word and how many times."""
    if word[0] == letter:
        print(letter, "found at index 1")
    if word[1] == letter:
        print(letter, "found at index 2")
    if word[2] == letter:
        print(letter, "found at index 3")
    if word[3] == letter:
        print(letter, "found at index 4")
    if word[4] == letter:
        print(letter, "found at index 5")
    # we want to check each index individually for a match to the inputted letter
    index: int = 0
    count: int = 0
    # need two variables here, one to count the matches, and one to bump the index up
    while index < len(word):
        # the len(word) could just be 5
        # I wanted to show what to use for other word input lengths
        if word[index] == letter:
            count += 1
        index += 1
    if count == 0:
        print("No instances of", letter, "found in", word)
    elif count == 1:
        print(count, "instance of", letter, "found in", word)
        # "instance" is different for count == 1
        # count could just be "1"
    else:
        print(count, "instances of", letter, "found in", word)
    # checking at each count variable to print a message if the count isn't 0 or 1
    return None


# return None is unnecessary


def main() -> None:
    """Makes the code run."""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
