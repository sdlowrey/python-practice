from datetime import datetime
from unittest import TestCase, main

from char_in.main import target_year


class TestUserInput(TestCase):
    def test_base_year(self):
        base_year = 2000
        current_age = 10
        target_age = 50
        wanted = 2040
        got = target_year(current_age, target_age, base_year=base_year)
        self.assertEqual(wanted, got)

    def test_this_year(self):
        current_year = datetime.now().year
        current_age = 30
        target_age = 50
        wanted = current_year + 20
        got = target_year(current_age, target_age)
        self.assertEqual(wanted, got)


if __name__ == '__main__':
    main()
