"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 2.3 display output with the string function -
#   write two lines of code:
#   the first one displays your name
#   the second displays your major
print("Trevor Price")
print("Web Development and Design")
# TODO 2.3 using quotes
#   Write a statement that displays
#   The dog says "woof!"
print('The dog say "woof!"')

# TODO 2.4 working with and printing variables
#   Declare a variable named age, and set the initial value to your age
#   Print the variable
#   Print the word age with a space and the variable
#   Assign the variable 42 to the age variable
#   Print the variable
#   Print the word age with a space and the variable
age = 23
print(age)
print("Age", age)
age = 42
print(age)
print("Age", age)
# TODO 2.6 keyboard input
#   Get the user to enter their name using an input statement and assign it to the variable name
#   Print a line that greets the user by name (Hello, Meri)
name = input("What's your name?")
print("Hello,", name)
# TODO 2.6 - 2.7 numeric input, performing calculations
#   Get the user to enter their age, store it as an integer
#   Print "This year you are ", age <-- please note, a comma creates a list of values
#   when using a comma in a print statement, you can mix numbers and strings
#   Add 1 to the age (age = age + 1)
#   Print "Next year you will be ", age
#   Remember - when printing a variable that holds numbers you need to convert it to a string
#   str(variable)
age = input("What's your age?")
print("This year you are", age)
age = int(age)+1
print("Next year you will be", age)

# TODO 2.7 performing calculations
#   Calculate 7 divided by 2, print the equation and the result
#   Calculate the remainder of 7 divided by 2, use the modulus operator, print the equation and the result
math = 7 / 2
print("7/2 =", math)
math = 7 % 2
print("7%2 =", math)
# TODO 2.7 data conversion
#   You will write equations as described below, the addition equation is done as a sample
#   You don't need to assign it to a variable

#   Sample:
#   Write an equation that adds an integer to an integer, display the equation and the result with a print statement

print("2 + 2 = " + str(2 + 2))

#   Write an equation that divides an integer by an integer, display the equation and the result with a print statement
print("5 / 5 = " + str(5 // 5))

#   Write an equation that divides an float by a float, display the equation and the result with a print statement
print("5.0 / 5.0 = " + str(5.0 / 5.0))

#   Write an equation that divides an float by an integer, display the equation and the result with a print statement
print("5.0 / 5 = " + str(5.0 / 5))

# TODO 2.8 Output
#   modify the following code to print on one line, without merging the lines of code. Separate the words with a hyphen
#   DO NOT MERGE INTO ONE LINE OF CODE, use escape characters
print('one-', end="")
print('two-', end="")
print('three')

# TODO 2.8 Output
#   Modify the following line of code to add tabs between the days of the week
print("Sunday\tMonday\tTuesday\tWednesday\tThursday\tFriday\tSaturday")


# TODO 2.8 Concatenating strings (Displaying Multiple Items with the + Operator)
#   Have the user enter their name
#   Greet the user, concatenate hello and their name into one string
name = input("What's your name?")
print("Hello "+str(name))

# TODO 2.8 Formatting numbers
#   Change the output so that it is formatted to display a minimum field width of 30
#   include commas, with only
#   two numbers showing to the right of the decimal point
#   example:
#                 6,548,974,897.57
number = 6548974897.5687979797
print('{:30,.2f}'.format(number))


# TODO 2.8 Formatting percentage
#   Format the following as a percentage with 2 as the precision
#   Sample:
#       percent = .25834
#       print(format(percent, '%'))
percentage = .7654
print('{0:.2%}'.format(percentage))
