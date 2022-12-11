class Validator():
    def validate_student_id(self):
        #check if 7 or less digits long if greater than 7 digits we ask user to re-enter the ID
        student_id_check = False
        while not student_id_check:
            try:
                int(self.id)
                if len(self.id) < 8:
                    student_id_check = True
                else:
                    student_id_check = False
            except:
                student_id_check = False
            #if the user inputs wrong information they will be prompted to re-enter info    
            if not student_id_check:
                self.id = input("Invalid input.\n Please re-enter Student ID: ")
    
    def validate_student_program_of_study(self):
        
        program_of_study_check = False
        while not program_of_study_check:
            try:
                #if a character is typed and if it is not an integer set check = to true
                if self.program_of_study and int(self.program_of_study) == False:
                    program_of_study_check = True
                #else if a character is blank 
                else:
                    program_of_study_check = False
            #The exception gets hit when the character is desired so we set check = to true        
            except:
                program_of_study_check = True
            
        #if the user inputs wrong information they will be prompted to re-enter info
            if not program_of_study_check:
                self.program_of_study = input("Invalid input.\n Please re-enter Program of Study: ")

    def validate_instructor_id(self):
        #check if 5 or less digits long if greater than 5 digits we ask user to re-enter the ID
        instructor_id_check = False
        while not instructor_id_check:
            try:
                int(self.id)
                if len(self.id) < 6:
                    instructor_id_check = True
                else:
                    instructor_id_check = False
            except:
                instructor_id_check = False
            #if the user inputs wrong information they will be prompted to re-enter info    
            if not instructor_id_check:
                self.id = input("Invalid input.\n Please re-enter Instructor ID: ")

    def validate_instructor_institution_graduated(self):

        institution_graduated_check = False
        while not institution_graduated_check:
            try:
                #if a character is typed and if it is not an integer set check = to true
                if self.institution_graduated and int(self.institution_graduated) == False:
                    institution_graduated_check = True
                #else if a character is blank 
                else:
                    institution_graduated_check = False
            #The exception gets hit when the character is desired so we set check = to true        
            except:
                institution_graduated_check = True
            
        #if the user inputs wrong information they will be prompted to re-enter info
            if not institution_graduated_check:
                self.institution_graduated = input("Invalid input.\n Please re-enter Institution graduated: ")

    def validate_instructor_degree_earned(self):

        degree_earned_check = False
        while not degree_earned_check:
            try:
                #if a character is typed and if it is not an integer set check = to true
                if self.degree_earned and int(self.degree_earned) == False:
                    degree_earned_check = True
                #else if a character is blank 
                else:
                    degree_earned_check = False
            #The exception gets hit when the character is desired so we set check = to true        
            except:
                degree_earned_check = True
            
        #if the user inputs wrong information they will be prompted to re-enter info
            if not degree_earned_check:
                self.degree_earned = input("Invalid input.\n Please re-enter Degree Earned: ")

    #same for both 
    def validate_name(self):
        #Creating TWO checks here BOTH need to be true to proceed.
        #set both the checks = to false
        name_validation_check = False
        name_validation_check2 = False
        #Create a list of delimter characters
        name_char_check = ['!','"', '@','#','$','%','^','&','*','(',')','_','=','+',',','<','>','/','?',';',':','[',']','{','}','\\']
        # Create a loop to check if both checks are true or if characters will need to be input again'
        while name_validation_check == False or name_validation_check2 == False:
            
            #First we check for if the name contains a number or a blank character
            while not name_validation_check:
                try:
                    #if a character is typed and if it is not an integer set check = to true
                    if self.name and int(self.name) == False:
                        name_validation_check = True
                    #else if a character is blank 
                    else:
                        #reset both checks to False
                        name_validation_check2 = False
                        name_validation_check = False
                #The exception gets hit when the character is desired so we set check = to true        
                except:
                    name_validation_check = True
                
            #if the user inputs wrong information they will be prompted to re-enter info
                if not name_validation_check:
                    self.name = input("Invalid input.\n Please re-enter your name: ")

            # Second we check for delimter characters
            while not name_validation_check2:
                for value in name_char_check:
                    if value in self.name:
                        #reset both checks to False
                        name_validation_check2 = False
                        name_validation_check = False
                        self.name = input("Invalid input.\n Please re-enter your name: ")
                    else:
                        name_validation_check2 = True
    #same for both
    def validate_email(self):
        #Creating TWO checks here BOTH need to be true to proceed.
        #set both the checks = to false
        email_validation_check = False
        email_validation_check2 = False
        #Create a list of delimter characters
        email_char_check = ['!','"',"'",'#','$','%','^','&','*','(',')','=','+',',','<','>','/','?',';',':','[',']','{','}','\\']
        # Create a loop to check if both checks are true or if characters will need to be input again'
        while email_validation_check == False or email_validation_check2 == False:
            
            #First we check for if the email contains a number or a blank character
            while not email_validation_check:
                try:
                    #if a character is typed set check = to true
                    if self.email:
                        email_validation_check = True
                    #else if a character is blank 
                    else:
                        #reset both checks to False
                        email_validation_check2 = False
                        email_validation_check = False
                #The exception gets hit when the character is desired so we set check = to true        
                except:
                    email_validation_check = True
                
            #if the user inputs wrong information they will be prompted to re-enter info
                if not email_validation_check:
                    self.email = input("Invalid input.\n Please re-enter your email: ")

            # Second we check for delimter characters
            while not email_validation_check2:
                for value in email_char_check:
                    if value in self.email:
                        #reset both checks to False
                        email_validation_check2 = False
                        email_validation_check = False
                        self.email = input("Invalid input.\n Please re-enter your email: ")
                    else:
                        email_validation_check2 = True

class Student(Validator):

    def displayinformation(self):
        print("Student records: ")
        print(self.college_records)
    
class Instructor(Validator):

    def displayinformation(self):
        print("Instructor records: ")
        print(self.college_records)

#Creating instances of the classes and adding college_records list to each
student = Student()
student.college_records = []

instructor = Instructor()
instructor.college_records = []


#made a quit variable
#made a variable to check for student or instructor
quit = ''
student_or_instructor = ''

#quit variable for user to input data and quit when prompted to
while quit != 'f' and quit != 'F':
    #asking if the user wants to input student or instructor information and keeps them in a loop if incorrectly inputted
    student_or_instructor = input("-S to input student information: \n-I to input instructor information: ")
    while student_or_instructor != 's' and student_or_instructor != 'S' and student_or_instructor != 'i' and student_or_instructor != 'I':
        student_or_instructor = input("incorrect input. \n-S for Student\n-I for instructor: ")

    #check if user is inputting student or instructor information
    if student_or_instructor == 's' or student_or_instructor == 'S':
        #Ask for user to input student ID if incorrect input student class calls Validator's
        # validate_student_id method which is being inherited by Student class
        student.id = input("Enter Student ID: ")
        student.validate_student_id()
        #Validate students program of study
        student.program_of_study = input("Enter program of study: ")
        student.validate_student_program_of_study()
        #Validate students name
        student.name = input("Enter your name: ")
        student.validate_name()
        #Validate students email
        student.email = input("Enter your email address: ")
        student.validate_email()

        #append all the student information to college_records
        student.college_records.append(student.id)
        student.college_records.append(student.program_of_study)
        student.college_records.append(student.name)
        student.college_records.append(student.email)
    #don't need to specify and can use else statement since loop keeps user inside if I or i isn't chosen
    else:
        #Ask for user to input instructor ID if incorrect input student class calls Validator's
        # validate_instructor_id method which is being inherited by Instructor class
        instructor.id = input("Enter Instructor ID: ")
        instructor.validate_instructor_id()
        #Validate instructors graduated institution
        instructor.institution_graduated = input("Enter Institution graduated from: ")
        instructor.validate_instructor_institution_graduated()
        #Validate instructors degree earned
        instructor.degree_earned = input("Enter highest degree earned: ")
        instructor.validate_instructor_degree_earned()
        #Validate instructors name
        instructor.name = input("Enter your name: ")
        instructor.validate_name()
        #Validate instructors email
        instructor.email = input("Enter your email address: ")
        instructor.validate_email()

        #append all instructor information to college_records
        instructor.college_records.append(instructor.id)
        instructor.college_records.append(instructor.institution_graduated)
        instructor.college_records.append(instructor.degree_earned)
        instructor.college_records.append(instructor.name)
        instructor.college_records.append(instructor.email)

    #prompted to see if user wants to stop inputting information
    quit = input("Press F to quit: ")

student.displayinformation()
instructor.displayinformation()