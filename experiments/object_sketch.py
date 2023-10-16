# Object heirarchy sketch for EasedServo class

from servo import Servo, servo2040
import easingfunctions as easing
import time

# Subclass of Servo
class EasedServo:
    """Subclass of Servo object to support easing functions."""

    # TODO: This should probably inherit from Servo rather than wrap it, but I'm rusty on Python syntax.
    # TODO: @property and @setter decorators work in Micropython now, I think? Would be neater.

    def __init__(self, pin, angle=90):
        """Basic constructor. Creates a Servo object and sets the angle to the given value, defaulting to 90."""
        self._servo = Servo(pin)
        self.angle = angle
        self._servo.value(angle)
        self._easing_function = easing.linear

    def ease_to(self, angle, duration, easing_function=easing.linear):
        """Sets the target angle and duration, and receives a function to use for easing."""
        self._start_angle = self.angle
        self._target_angle = angle
        self._easing_function = easing_function
        # Start a millisecond timer
        self._base_time = time.ticks_ms()
        self._duration = duration
        self._isMoving = True
        print (">>> Starting move to: " + str(angle) + " in " + str(duration) + "ms" +" using " + easing_function.__name__ + " easing.")
        # I don't think we actually need to do anything in here, just set up the variables.

    def update(self):
        """Handle servo angle updates."""
        # How far through the movement duration are we?
        proportion_complete = (time.ticks_ms() - self._base_time) / self._duration
        # print("Proportion complete: " + str(proportion_complete))
        # Calculate the new angle
        self.angle = self._easing_function(proportion_complete) * (self._target_angle - self._start_angle) + self._start_angle
        # Set the servo position
        self._servo.value(self.angle)
        # Are we done?
        if proportion_complete >= 1:
            self._isMoving = False


# Do if we're called directly
if __name__ == '__main__':
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

