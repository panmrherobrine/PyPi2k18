from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(270)

temp = round( sense.get_temperature(), 1 )

w = (255,255,255)
b = (0,0,0)
r = (255,0,0)






sense.show_message("GREETINGS FROM POLAND", scroll_speed=0.07, text_colour=r) # POZDROWIENIA
sleep(2)


if temp <= 15:
  n = (255, 255, 255)
  z = (200, 255, 255)
  s = (196, 196, 196)
  sl = (254, 255, 200)
  rysa = [
    n, n, n, n, s, s, n, n,
    n, sl, n, n, n, n, n, n,
    n, n, n, s, s, n, s, s,
    n, n, n, n, n, n, n, n,
    n, z, z, z, n, n, z, z,
    z, z, z, z, z, z, z, z,
    z, z, z, z, z, z, z, z,
    z, z, z, z, z, z, z, z
  ]
  sense.set_pixels(rysa)
elif temp >= 16 and temp <= 20:
  b = (0,0,0)
  u = (0,162,232)
  g = (0,138,0)
  d = (2,70,0)
  o = (124,78,52)
  rysb = [
      u, u, u, u, u, u, u, u,
      u, u, u, u, d, u, u, u,
      u, u, u, d, d, d, u, u,
      u, u, u, u, o, u, u, u,
      u, u, u, u, o, u, u, u,
      u, u, g, g, g, g, g, u,
      g, g, g, g, g, g, g, g,
      g, g, g, g, g, g, g, g
  ]
  sense.set_pixels(rysb)
elif temp >= 21:
    S = (255, 208, 0)
    P = (255, 255, 66)
    N = (0, 174, 255)
    K = (0, 147, 38)
    rysc = [
        S, S, N, N, N, N, N, N,
        S, N, N, N, N, K, N, N,
        N, N, N, N, K, K, N, N,
        N, N, N, N, N, K, K, N,
        N, N, P, P, N, K, N, N,
        N, P, P, P, P, P, P, P,
        P, P, P, P, P, P, P, P,
        P, P, P, P, P, P, P, P
    ]
    sense.set_pixels(rysc)



