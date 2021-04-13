from microbit import *

P0_MAX = 812
SIGNIFICANT = 3
CHARGING = Image("90000:09000:90000:00000:00000")
DISCHARGING = Image("00090:00009:00090:00000:00000")

diffs = [0 for i in range(10)]
sumd = 0
prevval = None

def trend(newval):
    global prevval, sumd

    if prevval is not None:
        olddiff = diffs.pop(0)
        newdiff = newval - prevval
        diffs.append(newdiff)
        sumd = sumd - olddiff + newdiff
        print(prevval, newval, newdiff, sumd)
    
    prevval = newval
    if abs(sumd) >= SIGNIFICANT:
        return sumd
    return 0  # no change
    
def barchart(y, v, vmax):
    v = min(v, vmax)
    leds = int(v * 5 / vmax)
    for x in range(leds):
        display.set_pixel(x, y, 9)
        
# main program
while True:
    reading = pin0.read_analog()
    display.clear()
    
    t = trend(reading)
    if t < 0:
        display.show(DISCHARGING)
    elif t > 0:
        display.show(CHARGING)
    
    barchart(4, reading, P0_MAX)
    
    if button_a.was_pressed():
        pin2.write_digital(0)  # off
    if button_b.was_pressed():
        pin2.write_digital(1)  # on
        
    sleep(1000)
