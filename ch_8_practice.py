"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""
print("----------Chapter 8.1----------")
# TODO 8.1 Basic string Operation
# Print all the characters from the name variable by accessing one character at a time

name = "John Jacob Jingleheimer Schmidt"
for character in name:
    print(character)
# Use the index to access and print the capital s in Schmidt from the variable name
print(name[24])
# Use the index with negative numbers to print the letters from the last name "Schmidt" in the
# name variable]
print(name[-7])
print("----------Chapter 8.2----------")
# TODO 8.2 String slicing
# use string slicing to assign the middle name "Jacob" from name to the variable middle, replace the ""

middle = name[5:10]
print(middle)

print("----------Chapter 8.3----------")
# TODO 8.3 Testing, Searching, and manipulating strings
# test to see if the string "Jacob" is in name
if middle in name:
    print("Yes")
else:
    print("No")
# test to see if the string "Michael" is in name
if "Michael" in name:
    print("Yes")
else:
    print("No")
# Test to see if name is a number
if name.isdigit():
    print("Yes")
else:
    print("No")
# Test to see if number is a number

number = 42
number = str(number)
number.isdigit()
if number.isdigit():
    print("Yes")
else:
    print("No")
# Search for "J" in name, replace with "j" (lower case)
name = name.replace('J', 'j')
print(name)
# split the string name into the variable name_list, replace the ""
name_list = name.split()
print(name_list)
