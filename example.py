from sense_emu import SenseHat
from colorzero import Color

sense  = SenseHat()

c = Color('green')
sense.clear(c.rgb_bytes)