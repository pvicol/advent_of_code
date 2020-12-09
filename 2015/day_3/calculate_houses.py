# Santa is delivering presents to an infinite two-dimensional grid of houses.

# He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

# However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

# For example:

# > delivers presents to 2 houses: one at the starting location, and one to the east.
# ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
# ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

def get_number_of_delivered_houses(directions: str) -> int:
    """
    Returns the number of houses that received at least one gift based on directions.
    """
    _tmp_houses = ["0,0"]
    _tmp_santa_position = [0,0]

    for direction in list(directions):
        if direction == "<":
            _tmp_santa_position[0] -= 1
        if direction == ">":
            _tmp_santa_position[0] += 1
        if direction == "^":
            _tmp_santa_position[1] += 1
        if direction == "v":
            _tmp_santa_position[1] -= 1

        value = f"{_tmp_santa_position[0]},{_tmp_santa_position[1]}"
        if not value in _tmp_houses:
            _tmp_houses.append(value)

    return len(_tmp_houses)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        temp_value = file.read()
    houses_list = get_number_of_delivered_houses(temp_value)
    print(houses_list)