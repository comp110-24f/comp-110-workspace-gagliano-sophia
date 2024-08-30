"""Small functions, calling other functions, small subprograms, main functions."""

__author__: str = "730699412"


def main_planner(guests: int) -> None:
    """Entrypoint of the program."""
    print("A Cozy Tea Party for", str(guests), "People!")
    # Spaces must occur within the strings for them to show up in the output.
    # You can also just add commas, rather than an addition of strings.
    print("Tea Bags:", tea_bags(people=guests))
    print("Treats:", treats(people=guests))
    print(
        "Cost:",
        "$"
        # Dollar sign is a separate string so as to be combined with the cost value.
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        ),
    )


# Worked out the definitions by working backwards from the concept of guests.


def tea_bags(people: int) -> int:
    """Return the number of tea bags based on the number of people."""
    return people * 2


def treats(people: int) -> int:
    """Computes the number of treats based on the number of teas."""
    return int(tea_bags(people=people) + people)


# Must use an addition function not just a call.


def cost(tea_count: int, treat_count: int) -> float:
    """Computes the cost of tea bags and treats."""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
# This needs to occur once at the end of the program, not after each line.
