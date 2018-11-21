from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(270)

temp = round( sense.get_temperature(), 1 )

w = (255,255,255)
b = (0,0,0)
r = (255,0,0)

picture = [
    b, b, w, w, w, w, b, b,
    b, w, b, b, b, b, w, b,
    b, w, b, w, w, b, w, b,
    b, w, b, b, b, b, w, b,
    b, b, w, w, w, w, b, b,
    b, b, w, w, w, w, b, b,
    b, w, w, w, w, w, w, b,
    b, w, w, w, w, w, w, b
]

sense.show_message("GREETINGS FROM POLAND", scroll_speed=0.07, text_colour=r)
sleep(2)
sense.set_pixels(picture)
