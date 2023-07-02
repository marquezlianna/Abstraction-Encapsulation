# Design a class named Fan to represent a fan.
class Fan:
    # The class contains:
    # Denote the fan speed.
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    # A constructor that creates a fan with the specified speed (default SLOW), radius (default 5), color (default blue), and on (default False).
    def __init__(self, speed=SLOW, radius=5, color='blue', on=False):
        # A private int data field named speed that specifies the speed of the fan.
        self.__speed = speed
        # A private bool data field named on that specifies whether the fan is on (the default is False).
        self.__on = on
        # A private float data field named radius that specifies the radius of the fan.
        self.__radius = radius
        # A private string data field named color that specifies the color of the fan.
        self.__color = color
