check = True
#empty dictionary created to gather data from information entered
employee_info = []
count = 0

#using count to keep the limit of information to less than 6 
while count < 6:
    #get employee ID
    emp_id = input("Enter your Employee ID: ")

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

    #get employee name and set a list of characters that can't be used
    name_char_check = ['!','"', '@','#','$','%','^','&','*','(',')','_','=','+',',','<','>','/','?',';',':','[',']','{','}','\\',
                       '0','1','2','3','4','5','6','7','8','9']

    emp_name = input("Enter your Name: ")
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

    #get employee email and set a list of characters that can't be used
    email_char_check = ['!','"',"'",'#','$','%','^','&','*','(',')','=','+',',','<','>','/','?',';',':','[',']','{','}','\\']
    emp_email = input("Enter your Email: ")

    #check if employee email contains any of the delimiter characters
    for value in email_char_check:
        if value in emp_email:
            check = False
    
    #same thing we did for name check
    while not check:
        emp_email = input("You have entered improper data. Please re-enter Employee Email: ")
        for value in email_char_check:
            if value in emp_email:
                check = False
                break
            else:
                check = True

    #get employee address and set a list of characters that can't be used
    address_char_check = ['!','"',"'", '@','$','%','^','&','*','_','=','+',',','<','>','?',';',':','[',']','{','}',]
    emp_address = input("Enter your Address(optional): ")

    #check if employee address contains any of the delimiter characters
    for value in address_char_check:
        if value in emp_address:
            check = False

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

    #incorrect symbol block
    while not check:
        emp_address = input("You have entered improper data. Please re-enter Employee Address: ")
        for value in address_char_check:
            if value in emp_address:
                check = False
                break
            else:
                check = True    

    #same thing we did for name check
    if not check:
        break

    #If address was provided and if it wasn't
    if address_check:
        print("Hello, " + str(emp_name) + " Your Employee ID is " + str(emp_id) + " and your email address is " +
        str(emp_email) + ". Your Address is " + str(emp_address))
    else:
        print("Hello, " + str(emp_name) + " Your Employee ID is " + str(emp_id) + " and your email address is " +
        str(emp_email) + ". You did not provide an address.")

    check = False

    #appending the information gathered and adding them to the empty dictionary we created earlier
    #we are structuring our dictionary in the database like structure with this format
    employee_info.append({'emp_id': emp_id, 'emp_name': emp_name, 'emp_email': emp_email, 'emp_address': emp_address})
    #this is adding +1 to our count so every time it completes it updates and will end once we hit 5 on the count
    count = count + 1

print(employee_info)