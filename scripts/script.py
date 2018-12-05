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
to20 = [
    b, b, w, w, w, w, b, b,
    b, w, b, b, b, b, w, b,
    b, w, b, w, w, b, w, b,
    b, w, b, b, b, b, w, b,
    b, b, w, w, w, w, b, b,
    b, b, w, w, w, w, b, b,
    b, w, w, w, w, w, w, b,
    b, w, w, w, w, w, w, b
]
wincyj25 = [
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
elif temp >= 16 and temp <= 20:
  sense.set_pixels(to38)
elif temp >= 21:
    
    S = (255, 208, 0) ## słońce
    P = (255, 255, 66) ## piasek
    N = (0, 174, 255) ## niebo
    K = (0, 147, 38) ## kakktus
    
    wincyj39 = [
        S, S, N, N, N, N, N, N,
        S, N, N, N, N, K, N, N,
        N, N, N, N, K, K, N, N,
        N, N, N, N, N, K, K, N,
        N, N, P, P, N, K, N, N,
        N, P, P, P, P, P, P, P,
        P, P, P, P, P, P, P, P,
        P, P, P, P, P, P, P, P
    ]
    
    sense.set_pixels(wincyj39)




