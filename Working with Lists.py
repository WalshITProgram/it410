courses_taken = ["com 300", "it 402", "com 320", "it 405", "mth 300", "com 340", "it 463", "it 407", "qm 202"]

courses_taken.sort()
for course in courses_taken:
    print("I have taken " + course.upper() + " at Walsh College")

courses_taken.append("it 408")
courses_taken.append("it 412")
courses_taken.append("it 460")
courses_taken.append("it 461")
courses_taken.sort()
print("This is my course of study with upcoming courses added: ")
print(courses_taken)

print("I do not have to take these courses: ")
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

print("\nI plan to take the following courses next term")
for course in courses_taken:
    print(course)

# Requirement 6 can we use modulo
numbers = list(range(1,1001))
numbers = [value % 6 == 0 for value in range(1, 1001)]
print(numbers)
# numbers = []
# for value in range(1, 1001):
#     divisible = value // 6
#     numbers.append(divisible)
# print(numbers)