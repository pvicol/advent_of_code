# For example:

# ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
# aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
# jchzalrnumimnmhp is naughty because it has no double letter.
# haegwjzuvuyypxyu is naughty because it contains the string xy.
# dvszwmarrgswjxmb is naughty because it contains only one vowel.


import unittest
from naughty_naughty import you_teasing_me

class TestNaughtyNaughty(unittest.TestCase):

    def setUp(self):

        # Set list of test cases
        self.test_houses_delivered_list = [
            ["ugknbfddgicrmopn", "nice"],
            ["aaa", "nice"],
            ["jchzalrnumimnmhp", "naughty"],
            ["haegwjzuvuyypxyu", "naughty"],
            ["dvszwmarrgswjxmb", "naughty"]
        ]

    def test_you_teasing_me(self):

        # Loop through test cases and check the answer
        for item in self.test_houses_delivered_list:
            with self.subTest():
                self.assertEqual(you_teasing_me(item[0]), item[1])

if __name__ == '__main__':
    unittest.main()