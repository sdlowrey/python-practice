import os
from unittest import TestCase

from text.words import build_index


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
