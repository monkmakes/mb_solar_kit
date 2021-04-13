from microbit import *

CHARGED = 818/2
DISCHARGED = 220
HOT = 23
COLD = 20
override = False
temp = 0

def read_temp():
    global temp
    temp = temperature()
    if override:
        temp = HOT

def fan_needed():
    return stored >= CHARGED and temp >= HOT

def fan_not_needed():
    return stored <= DISCHARGED or temp <= COLD

def fan_on():
    pin2.write_digital(1)
    display.show(Image.YES)

def fan_off():
    pin2.write_digital(0)
    display.show(Image.NO)

# main program
while True:
    # sensing
    stored = pin0.read_analog()
    if button_a.was_pressed():
        override = True
    if button_b.was_pressed():
        override = False
    read_temp()

    # control
    if fan_needed():
        fan_on()
    elif fan_not_needed():
        fan_off()

    print(stored, temp)
    sleep(1000)
