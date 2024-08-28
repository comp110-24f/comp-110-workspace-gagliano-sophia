"""My First Challenge Question"""

__author__ = "730699412"


def mimic(message: str) -> str:
    """Repeat message back."""
    return message


def main() -> None:
    """Main function to print mimic function."""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
