def draw_grid(x: int, y: int, state: int = 0) -> list:
    """
    Returns the code number required that has at least n number of zeros
    """
    lights = []
    for x in range(x + 1):
        lights.append([])
        for y in range(y + 1):
            lights[x].append(state)
    return lights

def get_details(input: str) -> dict:
    """
    Get command and other details
    """
    if input.startswith("turn on"):
        _tmp_instructions = input.replace("turn on ", "").split(" through ")
        return {
            "action": "turn on",
            "from": _tmp_instructions[0],
            "to": _tmp_instructions[1]
        }
    
    elif input.startswith("turn off"):
        _tmp_instructions = input.replace("turn off ", "").split(" through ")
        return {
            "action": "turn off",
            "from": _tmp_instructions[0],
            "to": _tmp_instructions[1]
        }
    elif input.startswith("toggle"):
        _tmp_instructions = input.replace("toggle ", "").split(" through ")
        return {
            "action": "toggle",
            "from": _tmp_instructions[0],
            "to": _tmp_instructions[1]
        }
    else:
        return None

def set_lights_on(from_number: str, to_number: str, grid: list):

    # Get coordinates
    x1,y1 = from_number.split(",")
    x2,y2 = to_number.split(",")

    # Loop through x axis
    for x in range(int(x1), int(x2) + 1):

        # Loop through y axis
        for y in range(int(y1), int(y2) + 1):
            grid[x][y] = 1
    
    return grid

def increase_light_brightness(from_number: str, to_number: str, grid: list):

    # Get coordinates
    x1,y1 = from_number.split(",")
    x2,y2 = to_number.split(",")

    # Loop through x axis
    for x in range(int(x1), int(x2) + 1):

        # Loop through y axis
        for y in range(int(y1), int(y2) + 1):
            grid[x][y] += 1
    
    return grid

def set_lights_off(from_number: str, to_number: str, grid: list):
    
    # Get coordinates
    x1,y1 = from_number.split(",")
    x2,y2 = to_number.split(",")

    # Loop through x axis
    for x in range(int(x1), int(x2) + 1):

        # Loop through y axis
        for y in range(int(y1), int(y2) + 1):
            grid[x][y] = 0
    
    return grid

def decrease_light_brightness(from_number: str, to_number: str, grid: list):
    
    # Get coordinates
    x1,y1 = from_number.split(",")
    x2,y2 = to_number.split(",")

    # Loop through x axis
    for x in range(int(x1), int(x2) + 1):

        # Loop through y axis
        for y in range(int(y1), int(y2) + 1):

            # Check if the number is greater than 0 and decrease by 1
            # This will ensure brightness doesn't go into negative
            if grid[x][y] > 0:
                grid[x][y] -= 1
    
    return grid

def set_toggle(from_number: str, to_number: str, grid: list):
    
    # Get coordinates
    x1,y1 = from_number.split(",")
    x2,y2 = to_number.split(",")

    # Loop through x axis
    for x in range(int(x1), int(x2) + 1):

        # Loop through y axis
        for y in range(int(y1), int(y2) + 1):
            if grid[x][y] == 0:
                grid[x][y] = 1
            else:
                grid[x][y] = 0
    
    return grid

def toggle_light_brightness(from_number: str, to_number: str, grid: list):
    
    # Get coordinates
    x1,y1 = from_number.split(",")
    x2,y2 = to_number.split(",")

    # Loop through x axis
    for x in range(int(x1), int(x2) + 1):

        # Loop through y axis
        for y in range(int(y1), int(y2) + 1):
            
            # Increase brightness by 2
            grid[x][y] += 2
    
    return grid

if __name__ == "__main__":

    # Get instructions from input file
    with open("input.txt", "r") as file:
        instructions = file.readlines()

    # grid = draw_grid(1000,1000)
    # for line in instructions:
    #     command = get_details(line.strip())
    #     if command["action"] == "turn on":
    #         grid = set_lights_on(command["from"], command["to"], grid)

    #     if command["action"] == "turn off":
    #         grid = set_lights_off(command["from"], command["to"], grid)

    #     if command["action"] == "toggle":
    #         grid = set_toggle(command["from"], command["to"], grid)
    
    # # Check for lights on
    # print(f"There are a total of {str(grid).count('1')} lights at the end")
    
    brightness_grid = draw_grid(1000,1000)    
    for line in instructions:
        command = get_details(line.strip())
        if command["action"] == "turn on":
            brightness_grid = increase_light_brightness(command["from"], command["to"], brightness_grid)

        if command["action"] == "turn off":
            brightness_grid = decrease_light_brightness(command["from"], command["to"], brightness_grid)

        if command["action"] == "toggle":
            brightness_grid = toggle_light_brightness(command["from"], command["to"], brightness_grid)
    
    # Check for lights on
    brightness = sum([sum(row) for row in brightness_grid])
    print(f"There are a total of {brightness} lights at the end")
