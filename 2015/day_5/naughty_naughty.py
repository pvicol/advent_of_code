# --- Day 5: Doesn't He Have Intern-Elves For This? ---
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

# --- Part Two ---
# Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

# Now, a nice string is one with all of the following properties:

# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
# For example:

# qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
# xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
# uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
# ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
# How many strings are nice under these new rules?

import re

def you_teasing_me(name: str, disallowed: list = ["ab", "cd", "pq", "xy"]) -> str:
    """
    Checks whether a name is nice or naughty based on a set of rules
    """

    # Let's see how nice this string is
    nice_threshold = 0

    # 1st rule, contains 3 vowels
    if re.search(r".*([aeiou].*){3}", name):
        nice_threshold += 1

    # 2nd rule, contains at least one letter that appears twice in a row
    if re.search(r"(.)\1", name):
        nice_threshold += 1

    # 3rd rule, disallowed string
    if re.search(r"|".join(disallowed), name):
        nice_threshold -= 1

    return "nice" if nice_threshold == 2 else "naughty"

def now_now(name: str) -> str:
    """
    Checks whether a name is nice or naughty based on a set of rules
    """
    # Let's see how nice this string is
    nice_threshold = 0

    # 1st rule, contains a pair of any two letters that appears at least twice in the string without overlapping

    if re.search(r"(..).*\1", name):
        nice_threshold += 1

    # 2nd rule, contains at least one letter which repeats with exactly one letter between them
    if re.search(r"(.).\1", name):
        nice_threshold += 1

    return "nice" if nice_threshold == 2 else "naughty"

if __name__ == "__main__":
    
    # Keep track of nice strings
    nice_strings = []
    nice_strings_revised = []

    # Read from input
    with open("input.txt", "r") as file:
        for string in file.readlines():
            if you_teasing_me(string) == "nice":
                nice_strings.append(string)

            if now_now(string) == "nice":
                nice_strings_revised.append(string)
    
    print(f"There are '{len(nice_strings)}' nice strings'")
    print(f"There are '{len(nice_strings_revised)}' nice strings'")