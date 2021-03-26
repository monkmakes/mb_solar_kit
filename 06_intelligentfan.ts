function fan_off () {
    pins.digitalWritePin(DigitalPin.P2, 0)
    basic.showIcon(IconNames.No)
}
function read_temp () {
    temp = input.temperature()
    if (override) {
        temp = HOT
    }
}
input.onButtonPressed(Button.A, function () {
    override = false
})
function fan_on () {
    pins.digitalWritePin(DigitalPin.P2, 1)
    basic.showIcon(IconNames.Yes)
}
input.onButtonPressed(Button.B, function () {
    override = true
})
function fan_notneeded () {
    return stored <= DISCHARGED || temp <= COLD
}
function fan_needed () {
    return stored >= CHARGED && temp >= HOT
}
let stored = 0
let override = false
let temp = 0
let COLD = 0
let HOT = 0
let DISCHARGED = 0
let CHARGED = 0
CHARGED = 818 / 2
DISCHARGED = 220
HOT = 23
COLD = 20
fan_off()
basic.forever(function () {
    stored = pins.analogReadPin(AnalogPin.P0)
    read_temp()
    serial.writeValue("s", stored)
    serial.writeValue("t", temp)
    if (fan_needed()) {
        fan_on()
    } else if (fan_notneeded()) {
        fan_off()
    }
    basic.pause(1000)
})