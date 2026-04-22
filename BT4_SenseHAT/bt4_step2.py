from sense_emu import SenseHat
import time

sense = SenseHat()

g = [0, 255, 0]    
b = [0, 0, 0]      
r = [255, 0, 0]   

invader = [
    b, b, g, b, b, g, b, b,
    b, b, b, g, g, b, b, b,
    b, g, g, g, g, g, g, b,
    g, g, r, g, g, r, g, g,
    g, g, g, g, g, g, g, g,
    g, b, g, g, g, g, b, g,
    g, b, g, b, b, g, b, g,
    b, b, b, g, g, b, b, b,
]

sense.set_pixels(invader)
print('Biểu tượng Space Invader đã hiển thị.')
time.sleep(5)
sense.clear()
