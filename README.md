# Abstraction-Encapsulation
# Fan Program

This program demonstrates the usage of the `Fan` class to create and manipulate fan objects. It utilizes the `pyfiglet` library for ASCII art text rendering and the `colorama` library for colored console output.

## Program Description

The program consists of two main components: the `Fan` class and the `TestFan` class.

### The `Fan` Class

The `Fan` class represents a fan object and contains the following attributes:

- `SLOW`, `MEDIUM`, `FAST`: Class constants representing the fan speeds.
- `__speed`: A private integer data field specifying the speed of the fan.
- `__on`: A private boolean data field indicating whether the fan is turned on.
- `__radius`: A private float data field specifying the radius of the fan.
- `__color`: A private string data field specifying the color of the fan.

The class provides getter and setter methods for each of the data fields.

### The `TestFan` Class

The `TestFan` class serves as a test program that creates two `Fan` objects and displays their properties.

The `TestFan` class creates two `Fan` objects with different configurations and then prints out their speed, radius, color, and on properties. It uses `pyfiglet` to create ASCII art headings for each fan object and `colorama` to display the text in different colors.

## How to Run the Program

To run the program, follow these steps:

1. Make sure you have Python and the required libraries installed.
2. Copy the program code into a Python file (e.g., `fan_program.py`).
3. Open a terminal or command prompt.
4. Navigate to the directory where the Python file is located.
5. Run the following command:
   ```
   python fan_program.py
   ```

The program will create the `Fan` objects, display their properties, and present the output in the console.

# Car Program

This program demonstrates the usage of the `Car` class to simulate the acceleration and braking of a car. It utilizes the `pyfiglet` library for ASCII art text rendering and the `colorama` library for colored console output.

## Program Description

The program consists of two main components: the `Car` class and the `main` function.

### The `Car` Class

The `Car` class represents a car object and contains the following attributes:

- `__year_model`: A private integer data field representing the year and model of the car.
- `__make`: A private string data field representing the make of the car.
- `__speed`: A private integer data field representing the current speed of the car.

The class provides the following methods:

- `__init__(self, year_model, make)`: Initializes a new instance of the `Car` class with the specified `year_model` and `make`.
- `accelerate(self)`: Increases the speed of the car by 5.
- `brake(self)`: Decreases the speed of the car by 5.
- `get_speed(self)`: Returns the current speed of the car.

### The `main` Function

The `main` function serves as the entry point of the program. It creates a `Car` object and demonstrates the acceleration and braking of the car. It uses `pyfiglet` to create ASCII art headings for each action and `colorama` to display the text in a different color.

## How to Run the Program

To run the program, follow these steps:

1. Make sure you have Python and the required libraries installed.
2. Copy the program code into a Python file (e.g., `car.py`).
3. Open a terminal or command prompt.
4. Navigate to the directory where the Python file is located.
5. Run the following command:
   ```
   python car.py
   ```

The program will create a `Car` object, simulate the acceleration and braking of the car, and display the current speed after each action.

