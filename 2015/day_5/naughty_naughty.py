# Santa needs help figuring out which strings in his text file are naughty or nice.

# A nice string is one with all of the following properties:

# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
# For example:

# ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
# aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
# jchzalrnumimnmhp is naughty because it has no double letter.
# haegwjzuvuyypxyu is naughty because it contains the string xy.
# dvszwmarrgswjxmb is naughty because it contains only one vowel.

import itertools


def you_teasing_me(name: str, vowels: list = ["a", "e", "i", "o", "u"], disallowed: list = ["ab", "cd", "pq", "xy"]) -> str:
    """
    Checks whether a name is nice or naughty based on a set of rules
    """

    # Let's see how nice this string is
    nice_threshold = 0

    # 1st rule, contains 3 vowels
    vowels_match = [letter for letter in name if letter in vowels]
    if len(vowels_match) >= 3:
        nice_threshold += 1

    # 2nd rule, contains at least one letter that appears twice in a row
    consecutive_group = ["".join(g) for _, g in itertools.groupby(name)]
    double_consecutive = [item for item in consecutive_group if len(item) >= 2]
    if double_consecutive:
        nice_threshold += 1

    # 3rd rule, disallowed string
    for rule in disallowed:
        if rule in name:
            nice_threshold -= 1

    return "nice" if nice_threshold == 2 else "naughty"

if __name__ == "__main__":
    
    # Keep track of nice strings
    nice_strings = []

    # Read from input
    with open("input.txt", "r") as file:
        for string in file.readlines():
            if you_teasing_me(string) == "nice":
                nice_strings.append(string)
    
    print(f"There are '{len(nice_strings)}' nice strings'")
