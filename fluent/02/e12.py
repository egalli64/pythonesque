"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Pattern Matching with Sequences - Example 2-9
"""


class InvalidCommand(Exception):
    pass


class Led:
    def __init__(self, brightness=0, red=0, green=0, blue=0):
        self.brightness = brightness
        self.red = red
        self.green = green
        self.blue = blue

    def set_brightness(self, brightness):
        self.brightness = brightness

    def set_color(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return f'Led({self.brightness}, {self.red}, {self.green}, {self.blue})'


class Robot:
    def __init__(self, name):
        self.name = name
        self.leds = [Led()]

    def handle_command(self, message):
        ident: int  # annotation for static analysis, a help for static type checkers

        # match the input message against the possible cases
        match message:
            # if the message has three items, and the first one is the string BEEPER
            # the second and third items are captured as frequency and times
            case ["BEEPER", frequency, times]:
                self.beep(frequency, times)
            case ["NECK", angle]:
                self.rotate_neck(angle)
            case ["LED", ident, brightness]:
                if 0 <= ident < len(self.leds):
                    self.leds[ident].set_brightness(brightness)
            case ["LED", ident, red, green, blue]:
                if 0 <= ident < len(self.leds):
                    self.leds[ident].set_color(red, green, blue)
            # default case
            case _:
                raise InvalidCommand(message)

    def beep(self, times, frequency):
        print(f"{self.name} beeps:", times, frequency)

    def rotate_neck(self, angle):
        print(f"{self.name} rotate neck:", angle)


if __name__ == "__main__":
    robot = Robot("Robot")
    print(robot.leds[0])

    robot.handle_command(["BEEPER", 3, 7])
    robot.handle_command(["NECK", 42])
    robot.handle_command(["LED", 0, 18])
    print(robot.leds[0])
    robot.handle_command(["LED", 0, 30, 60, 90])
    print(robot.leds[0])

    try:
        robot.handle_command(["UNKNOWN"])
    except InvalidCommand:
        print("Invalid Command")
