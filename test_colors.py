#!/usr/bin/env python3

import itertools as it


def test_colors():
    print()
    for foreground in it.chain(range(30, 38), range(90, 98)):
        for background in it.chain(range(40, 48), range(100, 108)):
            print(" \33[{:d};{:d}m{:d};{:<3d}\33[0m ".format(foreground, background, foreground, background), end="")
        print()
    print()


if __name__ == "__main__":
    test_colors()
