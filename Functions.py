#Functions

#function that accepts parameter for the inputs and meets all checks and returns the value
#if everything is good
def check_emp_id_func(emp_id):
    
    #check if 7 or less digits long if greater than 7 digits we ask user to re-enter the ID
    emp_id_check = False
    while not emp_id_check:
        if emp_id:
            try:
                int(emp_id)
                if len(emp_id) < 8:
                    emp_id_check = True
                else:
                    emp_id_check = False
                    
            except:
                emp_id_check = False
                
        else:
            emp_id_check = False
        

    #if the user inputs wrong information they will be prompted to re-enter info
        if not emp_id_check:
            emp_id = input("You have entered improper data. Please re-enter Employee ID: ")
    return emp_id

#function that accepts parameter for the inputs and meets all checks and returns the value
#if everything is good
def check_emp_name_func(emp_name):
    #checking to not allow blank values
    blank_name_check = False
    
    while not blank_name_check:
        if emp_name:
            try:
                if emp_name:
                    blank_name_check = True
                else:
                    blank_name_check = False
                    
            except:
                blank_name_check = False
                
        else:
            blank_name_check = False
        

    #if the user inputs wrong information they will be prompted to re-enter info
        if not blank_name_check:
            emp_name = input("You have entered improper data. Please re-enter Employee Name: ")

    #check if employee name contains any of the delimiter characters
    # get out of the for loop for name check 
    #while check is false we keep looping
    check = False
    while not check:
        for value in name_char_check:
            if value in emp_name:
                check = False
                break
            else:
                check = True
            
        if not check:
            emp_name = input("You have entered improper data. Please re-enter Employee Name: ")
    return emp_name

#function that accepts parameter for the inputs and meets all checks and returns the value
#if everything is good
def check_emp_email_func(emp_email):
    blank_email_check = False
    #checking to not allow blank values
    while not blank_email_check:
        if emp_email:
            try:
                if emp_email:
                    blank_email_check = True
                else:
                    blank_email_check = False
                    
            except:
                blank_email_check = False
                
        else:
            blank_email_check = False
        

    #if the user inputs wrong information they will be prompted to re-enter info
        if not blank_email_check:
            emp_email = input("You have entered improper data. Please re-enter Employee Email: ")

    #check if employee email contains any of the delimiter characters
    for value in email_char_check:
        if value in emp_email:
            check = False
            break
        else:
            check = True
    
    #same thing we did for name check
    while not check:
        emp_email = input("You have entered improper data. Please re-enter Employee Email: ")
        for value in email_char_check:
            if value in emp_email:
                check = False
                break
            else:
                check = True
    return emp_email

#function that accepts parameter for the inputs and meets all checks and returns the value
#if everything is good
def check_emp_address_func(emp_address):
    #check if employee address contains any of the delimiter characters
    for value in address_char_check:
        if value in emp_address:
            check = False
            break
        else:
            check = True

    #incorrect symbol block
    while not check:
        emp_address = input("You have entered improper data. Please re-enter Employee Address: ")
        for value in address_char_check:
            if value in emp_address:
                check = False
                break
            else:
                check = True
    return emp_address
    
#separated this part from the address check and put it into a function that when called checks
#if address was entered so that it accepts blank values and returns the appropriate prompt
def check_address_check_func():

    #since this is optional we check if user inputted anything, we then set it to 
    #true or false and move on to the next part
    address_check = False
    while not address_check:
        if emp_address:
            try: #incorrect symbol block
                address_check = True
            except:
                address_check = True    
        else: #not providing an address block  
            address_check = False
            break
    return address_check

#get employee name and set a list of characters that can't be used
name_char_check = ['!','"', '@','#','$','%','^','&','*','(',')','_','=','+',',','<','>','/','?',';',':','[',']','{','}','\\',
                       '0','1','2','3','4','5','6','7','8','9']
#get employee email and set a list of characters that can't be used
email_char_check = ['!','"',"'",'#','$','%','^','&','*','(',')','=','+',',','<','>','/','?',';',':','[',']','{','}','\\']

#get employee address and set a list of characters that can't be used
address_char_check = ['!','"',"'", '@','$','%','^','&','*','_','=','+',',','<','>','?',';',':','[',']','{','}',]


check = True
#empty dictionary created to gather data from information entered
employee_info = []
stop = ''
#using the length of employee_info to iterate through the loop and allowing user to quit
while len(employee_info) < 6 and stop != 'F' and stop != 'f':

#prompt for user input for employee ID and calls function
#function then accepts argument of the input variable
    emp_id = input("Enter your Employee ID: ")
    check_emp_id_func(emp_id)

#prompt for user input for employee name and calls function
#function then accepts argument of the input variable
    emp_name = input("Enter your Name: ")
    check_emp_name_func(emp_name)

#prompt for user input for employee email and calls function
#function then accepts argument of the input variable
    emp_email = input("Enter your Email: ")
    check_emp_email_func(emp_email)

#prompt for user input for employee address and calls function
#function then accepts argument of the input variable
    emp_address = input("Enter your Address(optional): ")
    check_emp_address_func(emp_address)
    
    #If address was provided and if it wasn't
    if check_address_check_func():
        print("Hello, " + str(emp_name) + " Your Employee ID is " + str(emp_id) + " and your email address is " +
        str(emp_email) + ". Your Address is " + str(emp_address))
    else:
        print("Hello, " + str(emp_name) + " Your Employee ID is " + str(emp_id) + " and your email address is " +
        str(emp_email) + ". You did not provide an address.")

    check = False

    #appending the information gathered and adding them to the empty dictionary we created earlier
    #we are structuring our dictionary in the database like structure with this format
    employee_info.append({'emp_id': emp_id, 'emp_name': emp_name, 'emp_email': emp_email, 'emp_address': emp_address})
    #user input to stop the program before 5 counts
    stop = input('Press F to stop: ')


print(employee_info)