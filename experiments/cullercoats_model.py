from Animation import EasedServo, QueueServo, easing
from machine import Button, LED
from time import sleep

button1 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
button2 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

myservos = QueueServoController()
servoGulls = QueueServo(servo2040.SERVO_1)
servoWaves = QueueServo(servo2040.SERVO_2)
servoLifeboat = QueueServo(servo2040.SERVO_3)

lifeboatLED = LED(25)

# TODO: Are interCappedNames a thing in Python? Or should we used underscores? queue_ease_to()

def animation1():
    # Sunny day
    # Swoop the seagulls
    servoGulls.queueEaseTo(90, 2000, easing.easeInOutCubic)
    servoGulls.queueEaseTo(-90, 2000, easing.easeInOutCubic)

    # Gentle waves
    servoWaves.queueAnimationSequence(animation_type='waves', from=30, to=90, speed=50)

def animation2():
    # Storm day
    # Blow seagulls away
    servoGulls.queueEaseTo(0, 500, easing.easeOutExpo)
    servoGulls.unblock(servoLifeboat)

    # Rough waves
    servoWaves.queueAnimationSequence(animation_type='waves', from=30, to=90, speed=250)

    # Launch the lifeboat
    lifeboatLED.flash(1)
    servoLifeboat.queueWaitFor(servoGulls)
    servoLifeboat.queueEaseTo(90, 2000, easing.easeInCubic)


def check_clicks():
    # Listen for button clicks

    if button1.pressed():
        servos.flushqueue()
        animation1()
    if button2.pressed():
        servos.flushqueue()
        animation2()

if __name__ == '__main__':
    while (True):
        check_clicks()
        # myservos.update()
        servoGulls.update()
        servoWaves.update()
        servoLifeboat.update()
        sleep(0.01)


# Example code for the queueing system
# using wait/unblock for synchronisation
servo1.queueEaseTo(180, 1000)
servo1.queueEaseTo(0, 1000)
servo1.queueEaseTo(180, 1000)
servo1.queueUnblock(servo2)
servo1.queueEaseTo(0, 1000)
servo1.queueEaseTo(180, 1000)


servo2.queueEaseTo(180, 5000)
servo2.queueWaitFor(servo1)
servo2.queueEaseTo(0, 1000)
servo2.queueEaseTo(180, 1000)

