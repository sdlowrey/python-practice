import re
from typing import Dict, Iterable, List, Tuple

WORD_RE = re.compile(r'\w+')


def build_index(text: Iterable) -> Dict[str, List[Tuple[int, int]]]:
    """Create an index of word counts from the input file.
    """
    index = {}
    for line_no, line in enumerate(text, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences
    return index
