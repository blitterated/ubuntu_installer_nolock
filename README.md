# Ubuntu Installer NoLock

While trying to install Ubuntu Studio, the screen would lock after a while unless I moved the mouse. I was also unable to get into a virtual terminal to unlock the installer session.[^vterm] So instead I pulled together a mouse jiggler to prevent the session from locking.

It uses CircuitPython on a Raspberry Pi Pico. The meat of it is based on a pico mouse jiggler article at Tom's Hardware.[^thjig]

I spent way too much time getting it to trace a circle, but it was fun nostalgia trip.[^ataribas]

## Dependencies

### CircuitPython

#### Bootloaders

* [All Bootloaders](https://circuitpython.org/downloads)
* [RPi Pico W](https://circuitpython.org/board/raspberry_pi_pico_w/)
* [RPi Pico](https://circuitpython.org/board/raspberry_pi_pico/)

#### Libraries

This only needs the adafruit_hid lib.

* [Full lib download](https://circuitpython.org/libraries)
* [adafruit_hid docs](https://docs.circuitpython.org/projects/hid/en/latest/)

[^vterm]: [Ask Ubuntu - Live CD asks for a username and password - vterm approach](https://askubuntu.com/a/1452011)

[^thjig]: [Tom's Hardware](https://www.tomshardware.com/how-to/diy-mouse-jiggler-raspberry-pi-pico)

[^ataribas]: [Atari Archives - Compute's 3rd Book of Atari - Ch. 4 Circles](https://www.atariarchives.org/c3ba/page153.php)