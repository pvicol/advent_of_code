# For example:

# If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
# If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....


import unittest
from stocking import get_zero_code

class TestStocking(unittest.TestCase):

    def setUp(self):

        # Set list of test cases
        self.test_stocking_list = [
            ["abcdef", 5, 609043],
            ["pqrstuv", 5, 1048970]
        ]

    def test_get_zero_code(self):

        # Loop through test cases and check the answer
        for item in self.test_stocking_list:
            with self.subTest():
                self.assertEqual(get_zero_code(code = item[0], zeros = item[1]),item[2])

if __name__ == '__main__':
    unittest.main()