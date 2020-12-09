# The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

# Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

# For example:

# A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.

# A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.

# All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?
# --- Part Two ---
# The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

# The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

# For example:

# A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
# A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.
# How many total feet of ribbon should they order?

def calculate_dimensions(l: int, w: int, h: int) -> int:
    """
    Function to calculate dimensions
    """
    
    # Calculate sides
    side_1 = l*w
    side_2 = w*h
    side_3 = h*l

    # Calculate based on dimensions
    wrapping_paper = 2 * side_1 + 2 * side_2 + 2 * side_3

    # Get minimum slack required based on smallest side

    slack_paper = min([side_1, side_2, side_3])
    
    # Return total wrapping paper required
    return wrapping_paper + slack_paper

def extract_dimensions(dimension: str) -> dict:
    """
    Function extracts length, width, and height from a string
    """

    # Exit if its not present
    if not dimension:
        raise Exception(f"Empty dimension {dimension}")
    else:
        
        # Split by x in the dimension list and assing values
        l, w, h = dimension.split("x")

        # Return dict with values extracted
        return {"l": int(l), "w": int(w), "h": int(h)}

def calculate_ribbon(l: int, w: int, h: int) -> int:
    """
    Returns the length of ribbon required based on present dimensions
    """
    # Get length to tie the present
    # The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face.

    # sort numbers, lowest to highest
    numbers = sorted([l, w, h])

    # use first 2 lowest numbers
    wrapping_length = numbers[0] * 2 + numbers[1] * 2

    # Get length for bow
    # the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present
    bow_length = l * w * h

    return bow_length + wrapping_length

if __name__ == "__main__":
    
    # Set example
    with open("input.txt", "r") as file:
        test_example = file.readlines()

    total_paper = 0
    for line in test_example:
        total_paper += calculate_dimensions(**extract_dimensions(line))

    # Print to screen
    print(total_paper)

    total_ribbon = 0
    for line in test_example:
        total_ribbon += calculate_ribbon(**extract_dimensions(line))

    # Print to screen
    print(total_ribbon)