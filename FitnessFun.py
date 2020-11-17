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

def convert_to_kilogram(user_weight):
    ''' convert user provided weight into kilograms '''
    converted_weight = float(user_weight) * 0.453592
    new_weight = int(converted_weight)
    return new_weight

def convert_to_meters(user_height):
    ''' convert user provided height into meters '''
    converted_height = float(user_height) * .0254
    return converted_height


def print_info():
    print("Your name is {} {}".format(first_name, last_name))
    print("Your birthday is {}-{}-{}".format(birthday.month,birthday.day,birthday.year))
    print("your weight in kilograms is {}.".format(convert_to_kilogram(weight)))
    print("Your height in meters is {}".format(convert_to_meters(height)))
    print("Your email address is {}.".format(email))

    print_info()

    def chest():
    ''' Allow the user to perform chest excercises'''
    print(" Great you have selected chest!")
    excercise_list = ['cable crossover', 'push_ups', 'dips', 'seated deck machine', 'plate press out' ]
    display_chest()
    selection = int(input("What excercise would u like to complete today? \n"))
    if selection < 1 or selection > 5:
        print("Invalid selection. Please try again.")
        chest()
    else:
        print("Alright you have selected {}.".format(excercise_list[selection-1]))
    amt, reps, sets, kilo = get_excercise_info()
    calculations(amt, reps, sets, kilo)
    
def arms():
    ''' Allow the user to perform arm excercises'''
    print("You have selected arms")
    excercise_list = ['Dumbell Preacher Curl', 'Cable Preacher Curl', 'Skull Crusher', 'Cable Triceps Pushdown', 'Barbell Bicep Curl' ]
    display_arms()
    selection = int(input("What excercise would u like to complete today? \n"))
    if selection < 1 or selection > 5:
        print("Invalid selection. Please try again.")
        arms()
    else:
        print("Alright you have selected {}.".format(excercise_list[selection-1]))
    amt, reps, sets, kilo = get_excercise_info()
    calculations(amt, reps, sets, kilo)

def back():
    ''' Allow the user to perform back excercises'''
    print("You have selected back")
    excercise_list = ['Kettlebell Swings', 'Inverted Row', 'Lat Pulldowns', 'Pull Ups', 'Barbell Deadlift' ]
    display_back()
    selection = int(input("What excercise would u like to complete today? \n"))
    if selection < 1 or selection > 5:
        print("Invalid selection. Please try again.")
        chest()
    else:
        print("Alright you have selected {}.".format(excercise_list[selection-1]))
    amt, reps, sets, kilo = get_excercise_info()
    calculations(amt, reps, sets, kilo)

def legs():
    ''' Allow the user to perform leg excercises'''
    print("You have selected legs")
    excercise_list = ['Front Squat', 'Deadlift', 'Walking Lunge', 'Leg Press', 'Goblet Squat' ]
    display_legs()
    selection = int(input("What excercise would u like to complete today? \n"))
    if selection < 1 or selection > 5:
        print("Invalid selection. Please try again.")
        chest()
    else:
        print("Alright you have selected {}.".format(excercise_list[selection-1]))
        amt, reps, sets, kilo = get_excercise_info()
        calculations(amt, reps, sets, kilo)

def abdominal():
    ''' Allow the user to perform abdominal excercises'''
    print("you have selected abdominal")
    excercise_list = ['Crunch', 'Reverse Crunch', 'Leg Raise', 'Plank', 'Mountain Climber' ]
    display_abdominal()
    selection = int(input("What excercise would u like to complete today? \n"))
    if selection < 1 or selection > 5:
        print("Invalid selection. Please try again.")
        chest()
    else:
        print("Alright you have selected {}.".format(excercise_list[selection-1]))
        amt, reps, sets, kilo = get_excercise_info()
        calculations(amt, reps, sets, kilo)
