from machine import Pin
from utime import sleep

print("Hello, World!")

ledRed = Pin (15, Pin.OUT)
ledYellow = Pin (2, Pin.OUT)
ledGreen = Pin (0, Pin.OUT)

while True:

    ledGreen.on()
    print("Green ON!")
    sleep(20.0)
    ledGreen.off()
    print("Green OFF!")
    sleep(0.5)

    ledYellow.on()
    print("Yellow ON!")
    sleep(10.0)
    ledYellow.off()
    print("Yellow OFF!")
    sleep(0.5)

    ledRed.on()
    print("Red ON!")
    sleep(7.0)
    ledRed.off()
    print("Red OFF!")
    sleep(0.5)