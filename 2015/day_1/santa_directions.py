# Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing.
# He starts on the ground floor (floor 0) and then follows the instructions one character at a time.
# 
# An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.
# 
# The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.
# 
# For example:
# 
# (()) and ()() both result in floor 0.
# ((( and (()(()( both result in floor 3.
# ))((((( also results in floor 3.
# ()) and ))( both result in floor -1 (the first basement level).
# ))) and )())()) both result in floor -3.
# To what floor do the instructions take Santa?

def get_floor(directions: str) -> int:
    """
    Gets the floor level the Santa is on.
    """
    _tmp_floor = 0
    for direction in directions:
        if direction == "(":
            _tmp_floor += 1
        elif direction == ")":
            _tmp_floor -= 1
        else:
            print("Unknown direction, skipping.")
    return _tmp_floor

def get_basement_notification(directions: str) -> int:
    """
    Gets the floor level the Santa is on.
    """
    _tmp_floor = 0
    for index, direction in enumerate(directions):
        if direction == "(":
            _tmp_floor += 1
        elif direction == ")":
            _tmp_floor -= 1
        else:
            print("Unknown direction, skipping.")

        if _tmp_floor == -1:
            return index + 1
    return _tmp_floor

if __name__ == "__main__":
    
    # Set example of GPS direction
    with open("input.txt", "r") as file:
        gps_directions = file.read()

    # Get the floor number
    floor = get_floor(gps_directions)
    basement_notification = get_basement_notification(gps_directions)

    # Print to screen
    print(floor)
    print(basement_notification)