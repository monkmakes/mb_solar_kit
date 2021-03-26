from microbit import *

TOC = 818  # c
BOC = 220

CHARGED = TOC/2
DISCHARGED = BOC
DISCHARGE_TIME = 250
RATE = (BOC - TOC) / DISCHARGE_TIME  # m
HOT = 23
COLD = 20
override = False
temp = 0

def remaining(v):
    return DISCHARGE_TIME - (v - TOC)/RATE

FONT = ( # WhaleySans font, 2x5 digits only
("99","99","99","99","99"),
("09","09","09","09","09"),
("99","09","99","90","99"),
("99","09","99","09","99"),
("90","90","99","09","09"),
("99","90","99","09","99"),
("99","90","99","99","99"),
("99","09","09","09","09"),
("99","99","00","99","99"),
("99","99","99","09","99")
)

def img(n):
    lg = FONT[int(n/10)]
    rg = FONT[int(n%10)]
    c = ""
    for r in range(5):
        c += lg[r] + "0" + rg[r]
        if r != 4:
            c += ':'
    return Image(c)

def digits(n):
    if n > 99: display.show(Image.CHESSBOARD)
    else: display.show(img(n))

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
    #display.show(Image.YES)

def fan_off():
    pin2.write_digital(0)
    #display.show(Image.NO)

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
    if fan_needed(): fan_on()
    elif fan_not_needed(): fan_off()

    # display
    digits(remaining(stored))
    print(stored, temp)
    sleep(500)
