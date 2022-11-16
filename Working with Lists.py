# Requirement 1 Created a list of all courses I have taken at Walsh
courses_taken = ["com 300", "it 402", "com 320", "it 405", "mth 300", "com 340", "it 463", "it 407", "qm 202"]

# Requirement 2 Sorted the list and printed each element with the courses in uppercase
courses_taken.sort()
for course in courses_taken:
    print("I have taken " + course.upper() + " at Walsh College")

# Requirement 3 Added the courses that I need to take and resorted the list. Also printed message to indicate that
courses_taken.append("it 408")
courses_taken.append("it 412")
courses_taken.append("it 460")
courses_taken.append("it 461")
courses_taken.sort()
print("\nThis is my course of study with upcoming courses added: ")
print(courses_taken)

# Requirement 4  Printed courses I don't need to take and removed the ones I didn't. 
print("\nI do not have to take these courses: ")
print(courses_taken[0])
print(courses_taken[1])
print(courses_taken[2])
print(courses_taken[3])
print(courses_taken[4])
print(courses_taken[5])
print(courses_taken[10])
print(courses_taken[11])
print(courses_taken[12])
del courses_taken[0:6]
del courses_taken[4:7]

# Requirement 5 Printed each course I am taking next semester in its own line
print("\nI plan to take the following courses next term")
for course in courses_taken:
    print(course)

# Requirement 6 Created a list of numbers 1-1000 that are divisible by 6
numbers = []
divisible = 0
for value in range(1, 167):
    divisible = divisible + 6
    numbers.append(divisible)

# Requirement 7 Printed the first 20 numbers in the list on its own line
print("\nHere are the 20 numbers divisble by 6: ")
for value in range(0, 20):
    print(numbers[value])

# Requirement 8 Created a variable for the largest number in the list
largest_number = max(numbers)

# Requirement 9 Printed the maximum value in the list
print("\nThe maximum value in the list is: " + str(largest_number))

# Requirement 10 Added the values of the 10th - 50th numbers in the numbers list
addition_result = sum(numbers[9:51])
print("\nHere is the sum of several values in the list: " + str(addition_result))

# Requirement 11 Overwrited the original courses_taken list with the numbers list we created in requirement 6
courses_taken = numbers
print("\n" + str(courses_taken))