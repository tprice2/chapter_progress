"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""
import pickle
print("----------Chapter 9.1----------")
# TODO 9.1 Dictionaries
# Finish creating the following dictionary by adding three more people and birthdays
birthdays = {'Meri': 'May 16', 'Kathy': 'July 14'}
birthdays['Trevor'] = 'June 28'
birthdays['Bob'] = 'May 2'
birthdays['Ken'] = 'December 12'
# Print Meri's Birthday
print(birthdays['Meri'] + '\n')
# Create an empty dictionary named registration
registration = dict()
# You will use the following dictionary for many of the remaining exercises

miles_ridden = {'June 1': 25, 'June 2': 20, 'June 3': 38, 'June 4': 12, 'June 5': 30, 'June 7': 25}

# print the keys and the values of miles_ridden using a for loop
for key in miles_ridden:
    print(key + ': ' + str(miles_ridden[key]))
print('\n')
# get the value for June 3 and print it, if not found display 'Entry not found', replace the ""
try:
    value = miles_ridden['June 3']
    print(str(value))
except KeyError:
    print('Entry not found')
# get the value for June 6 and print it, if not found display 'Entry not found' replace the ""
try:
    value = miles_ridden['June 6']
    print(str(value))
except KeyError:
    print('Entry not found')

# Use the items method to print the miles_ridden dictionary
print(miles_ridden.items())

# Use the keys method to print all of the keys in miles_ridden
print(miles_ridden.keys())
# Use the pop method to remove june 4 then print the contents of the dictionary
print(miles_ridden.pop('June 4', 'Not Found'))
print(miles_ridden)
# Use the values method to print the contents of the miles_ridden dictionary
print(miles_ridden.values())
print("----------Chapter 9.2----------")
# TODO 9.2 Sets
# Create an empty set named my_set
my_set = set()
# Create a set named days that contains the days of the week
days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = set(days_list)
# get the number of elements from the days set and print it
print(len(days))
# Remove Saturday and Sunday from the days set
days.remove('Saturday')
days.remove('Sunday')
# Determine if 'Mon' is in the days set
if 'Mon' in days:
    print("Yes, it's in the set.")
else:
    print("No, it's not in the set.")
print("----------Chapter 9.3----------")
# TODO 9.3 Serializing Objects (Pickling)

# import the pickle library
# Completed at top of page.
# create the output file log and open it for binary writing
log = open('log.txt', 'wb')
# pickle the miles_ridden dictionary and output it to the log file
pickle.dump(miles_ridden, log)
# close the log file
log.close()
