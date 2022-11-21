#Requirement 1
data_list = [1121, "Jackie Grainger", 22.22,
             1122, "Jignesh Thrakkar", 25.25,
             1127, "Dion Green", 28.75, False,
             24.32, 1132, "Jacob Gerber",
             "Sarah Sanderson", 23.45, 1137, True,
             "Brandon Heck", 1138, 25.84, True,
             1152, "David Toma", 22.65,
             23.75, 1157, "Charles King", False,
             "Jackie Grainger", 1121, 22.22, False,
             22.65, 1152, "David Toma"]

#Requirement 2
employee_numbers = []
employee_names = []
employee_salary = []

# Requirement 3 - Employee numbers list that removes duplicates and sorts them
for value in data_list:
    if value not in employee_names and value not in employee_numbers and value not in employee_salary:
        if type(value) is int:      #sorts for employee numbers and adds to respective list
            employee_numbers.append(value)
        elif type(value) is str:    #sorts for employee names and adds to respective list
            employee_names.append(value)
        elif type(value) is float:  #sorts for employee salary and adds to respective list
            employee_salary.append(value)

# Requirement 4 - Creating a new list that takes our salary list and multiplies 1.3 to it. Also raises a flag if someone's 
# salary is higher than 37.30
total_hourly_rate = []
for value in employee_salary:
    total_hourly_rate.append(value * 1.3)
if max(total_hourly_rate) >= 37.30:
    print("Someone's salary is a budget concern.")

# Requirement 5 - Creating a new list that adds the values between 28.15 and 30.65 to that list
underpaid_salaries = []
for value in total_hourly_rate:
    if value > 28.15 and value < 30.65:
        underpaid_salaries.append(value)

# Requirement 6 - Calculating the raises
# for each value in original float list
# -if hourly rate is between 22 and 24 apply 5% raise
# -if hourly rate is between 24 and 26 apply 4% raise
# -if hourly rate is between 26 and 28 apply 3% raise
# -all other rates get a 2% raise
# add these new values to a list called company_raises
company_raises = []
for value in employee_salary:
    if value > 22 and value < 24:
        company_raises.append(value * 1.05)
    elif value > 24 and value < 26:
        company_raises.append(value * 1.04)
    elif value > 26 and value < 28:
        company_raises.append(value * 1.03)
    else:
        company_raises.append(value * 1.02)

# Requirement 7 
# This will return values that are integers and are between 1126 to 1150 and they are even.
for value in data_list:
    if type(value) is int and value > 1126 and value < 1150 and value % 2 == 0:
        print(value)