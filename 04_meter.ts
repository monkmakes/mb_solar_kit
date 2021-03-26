input.onButtonPressed(Button.A, function () {
    pins.digitalWritePin(DigitalPin.P2, 0)
})
input.onButtonPressed(Button.B, function () {
    pins.digitalWritePin(DigitalPin.P2, 1)
})
basic.forever(function () {
    led.plotBarGraph(
    pins.analogReadPin(AnalogPin.P0),
    1023
    )
})