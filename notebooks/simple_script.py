#!/usr/bin/env python
"""A simple script to test the utils.RNG class by printing a sequence of random numbers.

Launch this script with `python simple_script.py`

The first line (`#!/usr/bin/env python`) is seen as a comment by python but as a special directive (shebang) by UNIX/Linux terminals. On a Linux system, you may directly execute the script, assuming it has the execute permission, with ./script.py

Ideally, we would like SEED and N to be configurable through command line arguments, but let's keep it simple for now.
"""
from modules.utils import RNG

SEED = 10
N = 10

def main():
    rng = RNG(SEED)
    random_sequence = rng.generate(N)
    print(random_sequence)

if __name__ == "__main__":
    main()
