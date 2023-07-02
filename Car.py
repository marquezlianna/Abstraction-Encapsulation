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

# Create a Car object
def main():
    car = Car(2023,"Lamborghini")

    # Accelerate the car five times and display the current speed after each acceleration
    print("The car is accelerating...")
    for _ in range(5):
        car.accelerate()
        print(f"Current speed: {car.get_speed()}")

    # Brake the car five times and display the current speed after each brake
    print("The car is braking...")
    for _ in range(5):
        car.brake()
        print(f"Current speed: {car.get_speed()}")

# Run the program
main()
