"""
In string, find all the characters that are unique (only occur once).

Do not consider upper/lower case or non-letters.
"""
from collections import defaultdict
from typing import Dict
import re
import sys


def count_characters(in_str: str) -> Dict:
    """Return a map of all characters. The character is the key, the number of occurrences.
    """
    counts = defaultdict(int)
    for c in in_str:
        if not c.isalpha():
            continue
        counts[c.lower()] += 1
    return counts


if __name__ == '__main__':
    # (unsafely) assume the first arg is a string
    in_text = sys.argv[1]
    print(f'input: {in_text}')
    counts = count_characters(in_text)
    for symbol, count in counts.items():
        print(f'{symbol}: {count}')
