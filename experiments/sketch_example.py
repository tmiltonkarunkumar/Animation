import object_sketch

# my_servo = EasedServo(2)
my_servo = EasedServo(servo2040.SERVO_1)

my_servo.ease_to(-90, 2000, easing.easeInOutCubic)

while my_servo._isMoving:
    my_servo.update()
    time.sleep(0.01)

time.sleep_ms(200)
my_servo.ease_to(90, 5000, easing.easeOutExpo)

while my_servo._isMoving:
    my_servo.update()
    time.sleep(0.01)

print("Done!")

