"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 7.2 Lists
# Create a list of days of the week, assign it to the variable days, remove """ """ to test


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# Create a list with 5 items, set them all to 0, use the Repetition Operator ( * )


# print the contents of your days list using the for operator


# print the list item that holds the value Saturday from the days list by using it's index


# set the size variable to hold the length of the list days using the len function

# concatenate the two following lists together, storing the value in list3 - remove the """ """ to test

print("----------Chapter 7.2----------")
list4 = [0] * 5
print(days)
print(days[5])
size = len(days)
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
list3 = list1 + list2
print(list3)

print("----------Chapter 7.3----------")
# TODO 7.3 List Slicing
# Slice the list days to select from Monday through Friday, inclusive, and assign the new list to work_days
# print work_days
work_days = days[0:5]
print(work_days)
print("----------Chapter 7.4----------")
# TODO 7.4 Finding items in Lists with the in Operator
# test to see if "Tue" is in the list days, print yes, Tue is in the list or no, Tue is not in the list
if 'Tue' in days:
    print("Yes, Tue is in the list")
else:
    print("Tue is not in the list")
print("----------Chapter 7.5----------")
# TODO 7.5 List Methods and Useful Built-in Functions
# Complete the following code to append the last three months of the year to the list months. Remove
# the """   """ to test, and print the contents of months

months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept"]
months.append("Oct")
months.append("Nov")
months.append("Dec")
print(months)
# get the index of "May" from the months list and print it on screen
print("Index of May: " + str(months.index("May")))

# sort list3 from the 7.2 exercise and print the results on screen
list3.sort()
print("Sorted list 3: " + str(list3))
# reverse the order of list 3
list3.reverse()
print("Reversed list 3: " + str(list3))
# delete the number 5 from list 3
list3.remove(5)
print("List 3 without 5" + str(list3))
# print the maximum item from list 3
print("Max in list 3: " + str(max(list3)))
print("----------Chapter 7.6----------")
# TODO 7.6 Copying Lists
# copy the list months to the variable months_of_the_year
# print the values in months_of_the_year
months_of_the_year = months.copy()
print(months_of_the_year)


print("----------Chapter 7.7----------")
# TODO 7.7 Processing lists
# total the values in list3 and print the results
total = sum(list3)
print("Total: " + str(total))
# get the average of values in list 3 and print the results
average = total / len(list3)
print("Average: " + str(average))
# open the file states in read mode, read the contents of the file into the list states_list and print the
# contents of states_list on screen
file_open = open("states.txt", "r")
states_list = file_open.read().split("\n")
print(states_list)
print("----------Chapter 7.8----------")
# TODO 7.8 Two-Dimensional Lists
# Create a two dimensional list that has the months of the year and the days in each month during a non leap year
# print the contents of the list
two_dimensional = [["Jan", 31], ["Feb", 28], ["Mar", 31], ["Apr", 30], ["May", 31], ["June", 30], ["July", 31], ["Aug", 31], ["Sept", 30], ["Oct", 31], ["Nov", 30], ["Dec", 31]]
print(two_dimensional)
# print just the values for index 3,0 and 3,1
print("----------Chapter 7.9----------")
# TODO 7.9 Tuples
# convert the months list to a tuple
tuple(months)
print(months)
