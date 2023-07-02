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

