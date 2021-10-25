import os
from unittest import TestCase

from text.words import build_index
from text.letters import count_characters


class WordTest(TestCase):
    def test_small(self):
        path = os.path.join(os.getcwd(), 'tests/data/small.txt')
        with open(path) as fp:
            index = build_index(fp)
        self.assertIn('thing', index.keys())
        self.assertEqual(len(index['thing']), 2)

    def test_medium(self):
        path = os.path.join(os.getcwd(), 'tests/data/medium.txt')
        with open(path) as fp:
            index = build_index(fp)
        self.assertIn('ipsum', index.keys())
        self.assertEqual(len(index['ipsum']), 6)


class LetterTest(TestCase):
    def test_short_string(self):
        counts = count_characters('This is a test string! Less than 99 characters.')
        self.assertEqual(counts['t'], 6)
        keys = counts.keys()
        self.assertNotIn('!', keys)
        self.assertNotIn('9', keys)

    def test_empty_string(self):
        counts = count_characters('')
        self.assertEqual(len(counts), 0)
