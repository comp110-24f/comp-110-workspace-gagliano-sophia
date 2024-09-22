"""Practice with Conditionals, Local Variables, and User Input."""

__author__: str = "730699412"


def guess_a_number() -> None:
    """Guessing a number."""
    secret: int = 7
    guess: int = int(input("Guess a number:"))
    print("Your guess was", guess)
    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is", secret)
    else:
        print("Your guess was too high! The secret number is", secret)
    return None


if __name__ == "__main__":
    guess_a_number()
