input.onButtonPressed(Button.A, function () {
    pins.digitalWritePin(DigitalPin.P2, 0)
})
input.onButtonPressed(Button.B, function () {
    pins.digitalWritePin(DigitalPin.P2, 1)
})
basic.showIcon(IconNames.Heart)
basic.forever(function () {
    serial.writeLine(convertToText(pins.analogReadPin(AnalogPin.P0)))
    basic.pause(1000)
})