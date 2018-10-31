"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 11.1 Introduction to Inheritance
# You are going to create a Dwelling class based on the Automobile
# Sample from the chapter


# create the class Dwelling, the __init__ method should accept number_of_rooms, square_feet, floors
class Dwelling:

    def __init__(self, number_of_rooms, square_feet, floors):
        self._number_of_rooms = number_of_rooms
        self._square_feet = square_feet
        self._floors = floors

# add the mutator for all of the data attributes (number_of_rooms, square_feet, floors)

    def set_number_of_rooms(self, number_of_rooms):
        self._number_of_rooms = number_of_rooms

    def set_square_feet(self, square_feet):
        self._square_feet = square_feet

    def set_floors(self, floors):
        self._floors = floors

# add the accessors for all of  the data attributes

    def get_number_of_floors(self):
        return self._number_of_rooms

    def get_square_feet(self):
        return self._square_feet

    def get_floors(self):
        return self._floors

# Create the class Single_family_home as a sub class of Dwelling
# The __init__ method should accept number_of_rooms, square_feet, floors, garage_type, yard_size
# call the superclass of Dwelling and pass the required arguments, remember to include self
# initialize the garage_type and yard_size attributes


class SingleFamilyHome(Dwelling):

    def __init__(self, number_of_rooms, square_feet, floors, yard_size, garage_type):
        Dwelling.__init__(self, number_of_rooms, square_feet, floors)
        self.garage_type = garage_type
        self.yard_size = yard_size

    def set_yard_size(self, yard_size):
        self._yard_size = yard_size

    def set_garage_type(self, garage_type):  # create the mutator and accessor methods for the garage_type and yard_size attributes
        self._garage_type = garage_type

    def get_garage_type(self):
        return self._garage_type

    def get_yard_size(self):
        return self._yard_size
# demonstrate the Single_family_home class, no need to import because you are in the same file

# create an object from the Single_family_home class with the following information:
# 6 rooms, 1200 square feet, 1 floor, single car garage, .25 acres
# Display the data using the accessor methods


# create the main function

# call the main function
def main():
    # These variables are what set each question, the possible answers, and the correct answers.
    q1 = SingleFamilyHome("6 rooms", "1200 square feet", "1 floor", "single car garage", ".25 acres")
    set_1 = [q1]

    for query in set_1:
        print("\n")
        print(query.get_number_of_floors())
        print(query.get_square_feet())
        print(query.get_floors())
        print(query.get_garage_type()) # Gets the question for each element in the set_1 list.
        print(query.get_yard_size())  # Gets the first answer for each element in the set_1 list.


main()


# TODO 11.2 Polymorphism
# Type in the mammal class from program 11-9    lines 1 - 22


# create a Mouse class as a sub class of the mammal class following the Dog example

# create a Bird class as a sub class of the mammal class following the Cat Example


# Follow the example in program 11-10 (no need to import, use main2 instead of main
# because there is already a main on this page) use the Mouse and Bird class that you created


