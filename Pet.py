# A class representing a pet with name, animal type, and age attributes.
class Pet:

    # Initializes the Pet object with default attribute values.
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    # Sets the name of the pet.
    def set_name(self, name):
        self.__name = name

    # Sets the animal type of the pet.
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    # Sets the age of the pet.
    def set_age(self, age):
        self.__age = age

    # Returns the name of the pet.
    def get_name(self):
        return self.__name

    # Returns the animal type of the pet.
    def get_animal_type(self):
        return self.__animal_type

    # Returns the age of the pet.
    def get_age(self):
        return self.__age

# Create an object of the Pet class
pet = Pet()

# Prompt the user to enter the name, type, and age of their pet
name = str(input("Enter the name of your pet: "))
animal_type = str(input("Enter the type of your pet: "))
age = str(input("Enter the age of your pet: "))



