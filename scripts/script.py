from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(270)

temp = round( sense.get_temperature(), 1 )

w = (255,255,255)
b = (0,0,0)
r = (255,0,0)

less15 = [
    b, b, w, w, w, w, b, b,
    b, w, b, b, b, b, w, b,
    b, w, b, w, w, b, w, b,
    b, w, b, b, b, b, w, b,
    b, b, w, w, w, w, b, b,
    b, b, w, w, w, w, b, b,
    b, w, w, w, w, w, w, b,
    b, w, w, w, w, w, w, b
]
to38 = [
    b, b, w, w, w, w, b, b,
    b, w, b, b, b, b, w, b,
    b, w, b, w, w, b, w, b,
    b, w, b, b, b, b, w, b,
    b, b, w, w, w, w, b, b,
    b, b, w, w, w, w, b, b,
    b, w, w, w, w, w, w, b,
    b, w, w, w, w, w, w, b
]
wincyj39 = [
    b, b, w, w, w, w, b, b,
    b, w, b, b, b, b, w, b,
    b, w, b, w, w, b, w, b,
    b, w, b, b, b, b, w, b,
    b, b, w, w, w, w, b, b,
    b, b, w, w, w, w, b, b,
    b, w, w, w, w, w, w, b,
    b, w, w, w, w, w, w, b
]

sense.show_message("GREETINGS FROM POLAND", scroll_speed=0.07, text_colour=r) # POZDROWIENIA
sleep(2)
# sense.set_pixels(picture) 

if temp <= 15:
  sense.set_pixels(less15)
elif temp >= 16 and temp <= 38:
  sense.set_pixels(to38)
elif temp >= 39:
  sense.set_pixels(wincyj39)




