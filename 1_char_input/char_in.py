#!/usr/bin/env python
# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

# Create a program that asks the user to enter their name and their age. Print out a message
# addressed to them that tells them the year that they will turn 100 years old.
#
# Extras:
#
# Add on to the previous program by asking the user for another number and printing out that many
# copies of the previous message. (Hint: order of operations exists in Python) Print out that
# many copies of the previous message on separate lines. (Hint: the string "\n is the same as
# pressing the ENTER button)
from datetime import datetime


MSG_FMT = """
Dear {name},

You will be 100 years old in {year}!

Sincerely, Puter.
"""


def target_year(age_now, age_target, base_year=None):
    if not base_year:
        base_year = datetime.now().year
    year_at_age = base_year - age_now + age_target
    return year_at_age


if __name__ == '__main__':
    name = raw_input('Your name > ')
    age = raw_input('Your age at the end of this year > ')
    year = target_year(int(age), 100)
    print(MSG_FMT.format(name=name, year=year))
