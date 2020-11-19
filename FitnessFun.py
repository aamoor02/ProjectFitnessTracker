import datetime 
import re

def check_birthday():
     '''Validate correct birthday format '''
     dob = input("What is your date of birth? Please enter in MM-DD-YYYY format.\n")
     try:
          birthday = datetime.datetime.strptime(dob, '%m-%d-%Y')
          return birthday
     except ValueError:
          print("You did not type your date of birth in the correct format")
          print("Please try again")
          return check_birthday()

def check_email():
    ''' Validate correct email formatting '''
    user_email = input("What is your email address? \n")
    if re.findall(r'[-\w\d+.]+@[-\w\d.]+', user_email):
        print("Your email address is valid!")
        list = re.findall(r'[-\w\d+.]+@[-\w\d.]+', user_email)
        return list[0]
    else:
        print("Your email address is invalid")
        return check_email()
    
     
# Global Variables
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
    '''Display information entered to the user'''
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

def display_chest():
    ''' Display chest excercises'''
    print (''' Here is a list of available excercises
                           1.   cable crossover \n
			   2.	push_ups  \n
			   3.	Dips \n
			   4.	seated deck machine \n
			   5.	plate press out  \n
''' )

def display_arms():
    ''' Display arm excercises'''
    print (''' Here is a list of available excercises
                           1.   dumbell preacher curl \n
			   2.	cable preacher curl  \n
			   3.	skull crusher \n
			   4.	cable triceps pushdown \n
			   5.	barbell_bicep_curl  \n
''' )

def display_back():
    ''' Display back excercises'''
    print (''' Here is a list of available excercises
                           1.   kettlebell swings \n
			   2.	inverted row  \n
			   3.	lat pulldowns \n
			   4.	Pull Up \n
			   5.	Barbell Deadlift  \n
''' )

def display_legs():
    ''' Display leg excercises'''
    print (''' Here is a list of available excercises
                           1.   Front Squat \n
			   2.	Deadlift  \n
			   3.	Walking Lunge \n
			   4.	Leg Press \n
			   5.	Goblet Squat  \n
''' )

def display_abdominal():
    ''' Display abdominal excercises'''
    print (''' Here is a list of available excercises
                           1.   Crunch \n
			   2.	Reverse Crunch  \n
			   3.	Leg Raise \n
			   4.	Plank \n
			   5.	Mountain Climber  \n
''' )


def get_excercise_info():
    ''' Gets excercise data from the user'''
    amount = int(input("what is the amount of weight in pounds? \n"))
    num_of_reps = int(input("What are the number of reps \n"))
    number_of_sets = int(input("What are the number of sets? \n"))
    weight_in_kilograms = convert_to_kilogram(amount)
    return amount, num_of_reps, number_of_sets, weight_in_kilograms


def calculations( weight, repetiton, numerous_sets, kilograms):
    '''Performs calculations for the user'''
    print("The amount of weight used for this excercise is {} pounds or {} kilograms".format(weight, kilograms))
    print("You have completed {} repetitions of this weight".format(repetiton))
    print("You have completed {} sets of these reps".format(numerous_sets))
    total_weight_pounds = weight * repetiton * numerous_sets
    total_weight_kilograms = kilograms * repetiton * numerous_sets
    print("The total amount of weight lifted for this excercise is {} pounds and {} kilograms".format(total_weight_pounds, total_weight_kilograms))

def get_choice():
    '''Gets the selection from the user'''
    print (''' Here is a list of available excercises
                           1.   Chest \n
			   2.	Arms  \n
			   3.	Back \n
			   4.	Legs \n
			   5.	Abdominal \n
''' )
    choice = int(input("What is your selection? \n"))
    if choice < 1 or choice > 5:
        print("Invalid selection. Please try again")
        return get_choice()
    else:
        return choice
   
#Get the selection from user
user_choice = get_choice()

#List of excercises
excercise_area = [chest, arms, back, legs, abdominal]

#Performs selected function after the users choice
excercise_area[user_choice -1]()



