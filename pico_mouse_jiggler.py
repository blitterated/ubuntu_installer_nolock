import usb_hid
from adafruit_hid.mouse import Mouse
from time import sleep
import math

m = Mouse(usb_hid.devices)

while True:
    print("\nJiggling\n")

    radius = 2.5
    radians = list(map(math.radians, range(360)))
    circle_coords = [(int(math.cos(r) * radius), int(math.sin(r) * radius)) for r in radians]
    for x, y in circle_coords:
        print(f"x:{x}, y:{y}")
        m.move(int(x), int(y), 0)
        sleep(.005)

    print("\nSleeping")
    sleep(10)
