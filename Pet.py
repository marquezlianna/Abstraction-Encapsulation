import tkinter as tk

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

# Create the Tkinter window
window = tk.Tk()
window.title("Pet Information")
window.config(bg="lightgray")

# Create an object of the Pet class
pet = Pet()

# Prompt the user to enter the name, type, and age of their pet
name_label = tk.Label(window, text="Enter the name of your pet:", font=("Arial", 12, "bold"), bg="lightgray")
name_label.pack()
name_entry = tk.Entry(window, font=("Arial", 12))
name_entry.pack()

animal_type_label = tk.Label(window, text="Enter the type of your pet:", font=("Arial", 12, "bold"), bg="lightgray")
animal_type_label.pack()
animal_type_entry = tk.Entry(window, font=("Arial", 12))
animal_type_entry.pack()

age_label = tk.Label(window, text="Enter the age of your pet:", font=("Arial", 12, "bold"), bg="lightgray")
age_label.pack()
age_entry = tk.Entry(window, font=("Arial", 12))
age_entry.pack()



# Set the attributes of the pet object
def submit():
    name = name_entry.get()
    animal_type = animal_type_entry.get()
    age = age_entry.get()

    pet.set_name(name)
    pet.set_animal_type(animal_type)
    pet.set_age(age)

    result_window = tk.Toplevel(window)
    result_window.title("Pet Information")
    result_window.config(bg="lightgray")

    # Display the pet's attributes
    name_label = tk.Label(result_window, text=f"Pet's Name: {pet.get_name()}", fg="blue", font=("Arial", 16, "bold"), bg="lightgray")
    name_label.pack(pady=10)

    animal_type_label = tk.Label(result_window, text=f"Pet's Animal Type: {pet.get_animal_type()}", fg="blue", font=("Arial", 16, "bold"), bg="lightgray")
    animal_type_label.pack(pady=10)

    age_label = tk.Label(result_window, text=f"Pet's Age: {pet.get_age()}", fg="blue", font=("Arial", 16, "bold"), bg="lightgray")
    age_label.pack(pady=10)

# Create the submit button
submit_button = tk.Button(window, text="Submit", command=submit, font=("Arial", 14, "bold"), bg="lightblue")
submit_button.pack(pady=10)

# Run the Program
window.mainloop()




