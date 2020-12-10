import unittest
import fire_hazard

class TestFireHazard(unittest.TestCase):

    def setUp(self):

        # Set list of test cases
        self.test_lights_instructions_end_to_end = [
            ["turn on 0,0 through 999,999", 1_000_000],
            ["toggle 0,0 through 999,0", 999_000],
            ["turn off 499,499 through 500,500", 998_996]
        ]
        self.test_lights_instructions_end_to_end_brightness = [
            ["turn on 0,0 through 0,0", 1],
            ["toggle 0,0 through 999,999", 2_000_000] # FIXME: AssertionError: 2000001 != 2000000
        ]
        self.test_lights_instructions_lights_on = [
            ["turn on 0,0 through 999,999", 1_000_000],
            ["turn on 0,0 through 999,0", 1000],
            ["turn on 499,499 through 500,500", 4]
        ]
        self.test_lights_instructions_lights_off = [
            ["turn on 0,0 through 999,999", 1_000_000],
            ["turn on 0,0 through 999,0", 1000],
            ["turn on 499,499 through 500,500", 4]
        ]

    def test_set_lights_on(self):
        # Loop through test cases and check the answer
        for item in self.test_lights_instructions_lights_on:
            with self.subTest():
                # Draw up grid
                self.grid = fire_hazard.draw_grid(1000,1000)

                action = fire_hazard.get_details(item[0])

                stats = fire_hazard.set_lights_on(action["from"], action["to"], self.grid)
                lights_on = str(stats).count("1")

                self.assertEqual(lights_on,item[1])

    def test_set_lights_off(self):
        # Loop through test cases and check the answer
        for item in self.test_lights_instructions_lights_off:
            with self.subTest():
                # Draw up grid
                self.grid = fire_hazard.draw_grid(1000,1000, 1)

                action = fire_hazard.get_details(item[0])

                stats = fire_hazard.set_lights_off(action["from"], action["to"], self.grid)
                lights_on = str(stats).count("0")

                self.assertEqual(lights_on,item[1])
    
    def test_end_to_end(self):
        # Draw up grid
        grid = fire_hazard.draw_grid(1000,1000)

        # Loop through test cases and check the answer
        for item in self.test_lights_instructions_end_to_end:
            with self.subTest():
                
                # Get action from string

                command = fire_hazard.get_details(item[0])
                if command["action"] == "turn on":
                    grid = fire_hazard.set_lights_on(command["from"], command["to"], grid)

                if command["action"] == "turn off":
                    grid = fire_hazard.set_lights_off(command["from"], command["to"], grid)

                if command["action"] == "toggle":
                    grid = fire_hazard.set_toggle(command["from"], command["to"], grid)

                lights_on = str(grid).count("1")

                self.assertEqual(lights_on,item[1])

    def test_end_to_end_brightness(self):
        # Draw up grid
        grid = fire_hazard.draw_grid(1000,1000)

        # Loop through test cases and check the answer
        for item in self.test_lights_instructions_end_to_end_brightness:
            with self.subTest():
                
                # Get action from string

                command = fire_hazard.get_details(item[0])
                if command["action"] == "turn on":
                    grid = fire_hazard.increase_light_brightness(command["from"], command["to"], grid)

                if command["action"] == "turn off":
                    grid = fire_hazard.decrease_light_brightness(command["from"], command["to"], grid)

                if command["action"] == "toggle":
                    grid = fire_hazard.toggle_light_brightness(command["from"], command["to"], grid)

                brightness = sum([sum(row) for row in grid])

                self.assertEqual(brightness,item[1])

if __name__ == '__main__':
    unittest.main()