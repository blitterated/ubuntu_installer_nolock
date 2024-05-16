import usb_hid
from adafruit_hid.mouse import Mouse
from time import sleep
import math

MOUSE = Mouse(usb_hid.devices)

# Set the size of the circle traced
RADIUS = 2.5

# Set how long it takes to trace a circle in seconds
DRAW_TIME = 1

# Set the delay between tracing circles in seconds
DELAY = 10

def build_circle_coords():
    # Build a list of radians for calculating points along the circumference
    radians = list(map(math.radians, range(360)))

    # Build a list of coordinate tuples that trace the circumference
    circle_coords = [(int(math.cos(r) * RADIUS), int(math.sin(r) * RADIUS)) for r in radians]

    return circle_coords

COORDS = build_circle_coords()
SLEEP_TIME = DRAW_TIME / len(COORDS)
NO_WHEEL = 0

while True:
    print("\nJiggling\n")

    for x, y in COORDS:
        print(f"x:{x}, y:{y}")
        MOUSE.move(x, y, NO_WHEEL)
        sleep(SLEEP_TIME)

    print("\nSleeping")
    sleep(DELAY)
