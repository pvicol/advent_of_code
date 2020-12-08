# (()) and ()() both result in floor 0.
# ((( and (()(()( both result in floor 3.
# ))((((( also results in floor 3.
# ()) and ))( both result in floor -1 (the first basement level).
# ))) and )())()) both result in floor -3.
# To what floor do the instructions take Santa?

import unittest
from santa_directions import get_floor

class TestGetFloor(unittest.TestCase):

    def setUp(self):

        # Set list of test cases
        self.test_get_floor_list = [
            ["(())", 0],
            [ "()()", 0],
            ["(((", 3],
            ["(()(()(", 3],
            ["))(((((", 3],
            ["())", -1],
            [ "))(", -1],
            [")))", -3],
            [")())())", -3]
        ]

    def test_get_floor(self):

        # Loop through test cases and check the floor number based on direction given
        for floor in self.test_get_floor_list:
            self.assertEqual(get_floor(floor[0]),floor[1])

if __name__ == '__main__':
    unittest.main()