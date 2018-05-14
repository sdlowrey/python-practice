from unittest import TestCase, main

from char_in.main import target_year


class TestUserInput(TestCase):
    def test_century_year(self):
        current_year = 2000
        current_age = 10
        target_age = 50
        wanted = 2040
        got = target_year(current_age, target_age, base_year=current_year)
        self.assertEqual(wanted, got)


if __name__ == '__main__':
    main()
