from microbit import *

P0_MAX = 812

def barchart(y, v, vmax):
    v = min(v, vmax)
    leds = int(v * 5 / vmax)
    for x in range(leds):
        display.set_pixel(x, y, 9)
        
# main program
while True:
    reading = pin0.read_analog()
    display.clear()
    barchart(4, reading, P0_MAX)
    
    if button_a.was_pressed():
        pin2.write_digital(0)  # off
    if button_b.was_pressed():
        pin2.write_digital(1)  # on
        
    sleep(1000)  # 1 second
