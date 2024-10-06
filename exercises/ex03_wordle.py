"""Ex03: Wordle game."""

__author__ = "730699412"


def input_guess(secret_word_len: int) -> str:
    """Prompt user to enter a guess of the correct length."""
    guess_input: str = input(f"Enter a {secret_word_len} character word:")
    while len(guess_input) != secret_word_len:
        guess_input = input(f"That wasn't {secret_word_len} chars! Try again:")
    return guess_input


# we want to take a user input here for the guess_input local variable and return it if
# it is actually the length of the secret word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Testing index of search parameter if it matches single_char parameter."""
    assert len(char_guess) == 1
    index: int = 0
    result: bool = False
    while index < len(secret_word):
        if char_guess == secret_word[index]:
            result = True
        index += 1
        # while loop used to make sure the character at that index is at all within
        # the secret word
    return result


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(user_guess: str, word: str) -> str:
    """Determines the correctness + placement of letters of a guess of a secret word."""
    assert len(user_guess) == len(word)
    index: int = 0
    boxes: str = ""
    while index < len(word):
        if user_guess[index] == word[index]:
            boxes += GREEN_BOX
        elif contains_char(secret_word=word, char_guess=user_guess[index]) is True:
            boxes += YELLOW_BOX
        elif contains_char(secret_word=word, char_guess=user_guess[index]) is False:
            boxes += WHITE_BOX
            # this is where we use the contains_char function
            # it is used to determine the difference between being somewhat correct and
            # not correct at all regarding the placement of letters
        index += 1
    return boxes


# had to use a separate local variable (boxes) to make sure the output was a returned
# horizontal string and not a vertically printed string


def main(secret: str) -> None:
    """Entrypoint and game loop."""
    turns: int = 1
    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        input: str = input_guess(secret_word_len=len(secret))
        # had to declare a local variable to prevent the function from asking for
        # a word input twice
        print(emojified(user_guess=input, word=secret))
        if input == secret:
            print(f"You won in {turns}/6 turns!")
            return None
        # use return instead of exit to prevent the function from harshly stopping
        turns += 1
    if turns > 6:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
