"""Coordinates file in CQ04"""

__author__ = "730699412"


def get_coords(xs: str, ys: str) -> None:
    """Print the formatted pairs of each character."""
    xindex: int = 0
    yindex: int = 0
    while xindex < len(xs):
        while yindex < len(ys):
            print("(" + xs[xindex] + ", " + ys[yindex] + ")")
            yindex += 1
        yindex = 0
        xindex += 1
