# A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.

# A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.

# All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

import unittest
from wrapping_paper import calculate_dimensions, extract_dimensions

class TestGetFloor(unittest.TestCase):

    def setUp(self):

        # Set list of test cases
        self.test_dimensions_list = [
            [{"l": 2, "w": 3, "h": 4}, 58],
            [{"l": 1, "w": 1, "h": 10}, 43]
            
        ]

        self.test_extract_dimensions_list = [
            ["29x13x26", {"l": 29, "w": 13, "h": 26}],
            ["24x28x28", {"l": 24, "w": 28, "h": 28}],
        ]

    def test_calculate_dimensions(self):

        # Loop through test cases and check the wrapping paper needed based on dimensions given
        for item in self.test_dimensions_list:
            with self.subTest():
                # Pass dict as keyword arguments to the function instead of specifying each
                self.assertEqual(calculate_dimensions(**item[0]), item[1])
    
    def test_extract_dimensions(self):
        
        # Loop through test cases
        for item in self.test_extract_dimensions_list:
            with self.subTest():
                self.assertEqual(extract_dimensions(item[0]), item[1])

if __name__ == '__main__':
    unittest.main()