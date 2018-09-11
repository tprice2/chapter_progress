# Complete all of the TODO directions
# The number next to the TODO represents the chapter
# and section that explain the required code
# Your file should compile error free
# Submit your completed file

# TODO 4.2 A condition controlled loop
# write a loop that will change the variable in num by subtracting 1
# then print the variable. Keep looping until the num = 0 (While num > 0)
num = 10
# write your code here, the variable needs to exist before
# you test it
while num > 0:
    num = num-1
    print(num)
# TODO 4.3 the For Loop
# Use a for loop with a list of the days of the week, print each day
# of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for x in days:
    print(x)
# TODO 4.3 the for loop - range function
# use the range function to print the numbers from 1 to 10
for i in range(1, 11):
    print(i)
# TODO 4.4 a running total
# Have the user enter 5 numbers, provide a total at the end
# You can assume integers
count = 0
total = 0
while count < 5:
    number = int(input("Enter a number:"))
    count = count+1
    total = total + number
print("Total = " + str(total))
# TODO 4.5 Sentinel Value
# Create a variable to store a total amount
# Create a variable to store a count of the numbers entered
# Have the user enter test scores until a sentinel value of -1 is
# entered.
# Display the total, the count and the average (total / count)
total2 = 0
count2 = 0
number = 0
while number != -1:
    number = int(input("Enter a number:"))
    count2 = count2 + 1
    total2 = total2 + number
    average = total2/count2
    print("Count: " + str(count2))
    print("Total: " + str(total2))
    print("Average: " + str(average))
print("Program Finished")
# TODO 4.6 validating data
# Ask the user to enter a number between 1 and 10.
# Use a while loop to force the user to repeat the
# prompt until the user enters a valid number. Test with
# both valid and invalid data
number = int(input("Please enter a number between 1 and 10:"))
while number < 1 or number > 10:
    number = int(input("Incorrect, please enter a number between 1 and 10:"))
