# Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

# To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

# For example:

# If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
# If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....

import itertools
import hashlib

def get_zero_code(zeros: int, code = None) -> int:
    """
    Returns the code number required that has at least n number of zeros
    """
    if not code:
        code = ""

    for number in itertools.count():
        _tmp_code_val = hashlib.md5(f"{code}{number}".encode('utf-8')).hexdigest()
        if _tmp_code_val.startswith("0" * zeros):
            return number


if __name__ == "__main__":
    
    # 5 zeros
    temp_value = "yzbqklnj"
    temp_result = get_zero_code(code = temp_value, zeros = 5)
    print(temp_result)

    # 6 zeros
    temp_value = "yzbqklnj"
    temp_result = get_zero_code(code = temp_value, zeros = 6)
    print(temp_result)