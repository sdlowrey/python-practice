"""
In string, find all the characters that are unique (only occur once).

Do not consider upper/lower case or non-letters.
"""
from collections import defaultdict
from typing import Dict
import sys


def count_characters(in_str: str) -> Dict:
    """Return a map of all characters. The character is the key, the number of occurrences.
    """
    counts = defaultdict(int)
    for c in in_str:
        counts[c.lower()] += 1
    return counts


if __name__ == '__main__':
    arg1 = sys.argv[1]
    chars = count_characters(arg1)
    for symbol, count in chars.items():
        print(f'{symbol}: {count}')
