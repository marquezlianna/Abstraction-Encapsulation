# Create a class representing a car
class Car:
    # Initializes a new instance of the Car class.
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # Increases the speed of the car by 5.
    def accelerate(self):
        self.__speed += 5

    # Decreases the speed of the car by 5.
    def brake(self):
        self.__speed -= 5

    # Returns the current speed of the car.
    def get_speed(self):
        return self.__speed
