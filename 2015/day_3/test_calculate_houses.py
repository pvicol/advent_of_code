# For example:

# > delivers presents to 2 houses: one at the starting location, and one to the east.
# ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
# ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.


import unittest
from calculate_houses import get_number_of_delivered_houses, get_number_of_delivered_houses_with_help

class TestCalculateHouses(unittest.TestCase):

    def setUp(self):

        # Set list of test cases
        self.test_houses_delivered_list = [
            ["^v^v^v^v^v", 2],
            [ "^>v<", 4],
            [">", 2]
        ]

        self.test_houses_delivered_list_part_2 = [
            ["^v", 3],
            [ "^>v<", 3],
            ["^v^v^v^v^v", 11]
        ]

    def test_get_number_of_delivered_houses(self):

        # Loop through test cases and check the answer
        for item in self.test_houses_delivered_list:
            with self.subTest():
                self.assertEqual(get_number_of_delivered_houses(item[0]),item[1])

    def test_get_number_of_delivered_houses_with_help(self):

        # Loop through test cases and check the answer
        for item in self.test_houses_delivered_list_part_2:
            with self.subTest():
                self.assertEqual(get_number_of_delivered_houses_with_help(item[0]),item[1])

if __name__ == '__main__':
    unittest.main()