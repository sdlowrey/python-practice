import os

from text.words import build_index
from text.letters import count_characters


class WordTest:
    def test_small(self):
        path = os.path.join(os.getcwd(), 'tests/data/small.txt')
        with open(path) as fp:
            index = build_index(fp)
        assert 'thing' in index.keys()
        assert len(index['thing']) == 2

    def test_medium(self):
        path = os.path.join(os.getcwd(), 'tests/data/medium.txt')
        with open(path) as fp:
            index = build_index(fp)
        assert 'ipsum' in index.keys()
        assert len(index['ipsum']) == 6


class LetterTest:
    def test_short_string(self):
        counts = count_characters('This is a test string! Less than 99 characters.')
        assert counts['t'] == 6
        keys = counts.keys()
        assert '!' not in keys
        assert '9' not in keys

    def test_empty_string(self):
        counts = count_characters('')
        assert len(counts) == 0
