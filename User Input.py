check = True

while check:
    #get employee ID
    emp_id = input("Enter your Employee ID: ")

    #check if 7 or less digits long if greater than 7 digits break out of while loop (terminate program)
    emp_id_check = False
    while not emp_id_check:
        if emp_id:
            try:
                int(emp_id)
                if len(emp_id) < 8:
                    emp_id_check = True
                else:
                    emp_id_check = False
                    break
            except:
                emp_id_check = False
                break
        else:
            emp_id_check = False
            break

    #if the user doesn't input anything it'll cause the program to terminate
    if not emp_id_check:
        break

    #get employee name and set a list of characters that can't be used
    name_char_check = ['!','"', '@','#','$','%','^','&','*','(',')','_','=','+',',','<','>','/','?',';',':','[',']','{','}','\\',
                       '0','1','2','3','4','5','6','7','8','9']

    emp_name = input("Enter your Name: ")
    #check if employee name contains any of the delimiter characters
    for value in name_char_check:
        if value in emp_name:
            check = False
    #check to see if employee name is a number, if it is then program terminates
    emp_name_check = False
    while not emp_name_check:
        if emp_name:
            try:
                int(emp_name)
                break
            except:
                emp_name_check = True
                break
        else:
            emp_name_check = False
            break
    
    if not emp_name_check:
        break
    
    # get out of the for loop for name check and check to see if check
    # is still true if not then break out of while loop (terminate program)
    if not check:
        break

    #get employee email and set a list of characters that can't be used
    email_char_check = ['!','"',"'",'#','$','%','^','&','*','(',')','=','+',',','<','>','/','?',';',':','[',']','{','}','\\']
    emp_email = input("Enter your Email: ")

    #check if employee email contains any of the delimiter characters
    for value in email_char_check:
        if value in emp_email:
            check = False
    
    email_check = False
    while not email_check:
        if emp_email:
            try:
                email_check = True
                break
            except:
                email_check = True
                break
        else:
            email_check = False
            break
    
    if not email_check:
        break
    
    #same thing we did for name check
    if not check:
        break

    #get employee address and set a list of characters that can't be used
    address_char_check = ['!','"',"'", '@','$','%','^','&','*','_','=','+',',','<','>','?',';',':','[',']','{','}',]
    emp_address = input("Enter your Address(optional): ")

    #check if employee address contains any of the delimiter characters
    for value in address_char_check:
        if value in emp_address:
            check = False

    address_check = False
    while not address_check:
        if emp_address:
            try:
                address_check = True
                break
            except:
                address_check = True
                break
        else:
            address_check = False
            break

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
