import datetime 
import re

def check_birthday():
     dob = input("What is your date of birth? Please enter in MM-DD-YYYY format.\n")
     try:
          birthday = datetime.datetime.strptime(dob, '%m-%d-%Y')
          return birthday
     except ValueError:
          print("You did not type your date of birth in the correct format")
          print("Please try again")
          check_birthday()

def check_email():
    ''' Validate correct email formatting '''
    user_email = input("What is your email address? \n")
    if re.findall(r'[-\w\d+.]+@[-\w\d.]+', user_email):
        print("Your email address is valid!")
        list = re.findall(r'[-\w\d+.]+@[-\w\d.]+', user_email)
        return list[0]
    else:
        print("Your email address is invalid")
        check_email()



first_name = input('what is your first name?\n').upper()
last_name = input('what is your last name?\n').upper()
birthday = check_birthday()
height = input('what is your height in inches?\n')
weight = input('what is your weight in pounds?\n')
email = check_email()