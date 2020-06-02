
# Code by Jason Adams

# Day 2 Exercises

''' 1. Create a function that uses the year of birth of the 
user as an argument and prints their age to the console. 
Test it on a few years. '''

''' I'm expanding it to take the full birthdate so age will 
be exact '''

from datetime import datetime

def age_from_birthdate(day, month, year):
    now = datetime.now()
    yeardiff = now.year - year
    monthdiff = now.month - month
    daydiff = now.day - day
    if monthdiff>0:
        age = yeardiff
    if monthdiff<0:
        age = yeardiff-1
    if monthdiff==0:
        if daydiff>0:
            age = yeardiff
        if daydiff<0:
            age = yeardiff-1
        if daydiff==0:
            print("Happy birthday!")
            age = yeardiff
    print(f"Your age is {age}")

age_from_birthdate(13, 4, 1990)

age_from_birthdate(20, 6, 1989)

age_from_birthdate(1, 12, 1995)

age_from_birthdate(2, 6, 2010)



''' 2. Upgrade the previous script to ask the user 
for their year of birth as input when the script is 
run, and print their age to the console. '''

def age_from_birthdate2():
    year = input("Enter the year in which you were born: ")
    month = input("Enter the month in which you were born as a number: ")
    day = input("Enter the day of the month in which you were born: ")
    year = int(year)
    month = int(month)
    day = int(day)
    now = datetime.now()
    yeardiff = now.year - year
    monthdiff = now.month - month
    daydiff = now.day - day
    if monthdiff>0:
        age = yeardiff
    if monthdiff<0:
        age = yeardiff-1
    if monthdiff==0:
        if daydiff>0:
            age = yeardiff
        if daydiff<0:
            age = yeardiff-1
        if daydiff==0:
            print("Happy birthday!")
            age = yeardiff
    print("Your age is " + str(age))

age_from_birthdate2()



''' 3. Create a function with an if/else conditional 
statement. Try nesting another if/else inside of the 
first "if" branch.'''

''' I'm going to change my exercise 1 function to fit this '''

def age_from_birthdate3(day, month, year):
    now = datetime.now()
    yeardiff = now.year - year
    monthdiff = now.month - month
    daydiff = now.day - day
    if monthdiff>0:
        age = yeardiff
    else:
        if monthdiff<0:
            age = yeardiff-1
        else:                
            if daydiff>0:
                age = yeardiff
            else:
                if daydiff<0:
                    age = yeardiff-1
                else:
                    print("Happy birthday!")
                    age = yeardiff
    print(f"Your age is {age}")

age_from_birthdate3(13, 4, 1990)

age_from_birthdate3(20, 6, 1989)

age_from_birthdate3(1, 12, 1995)

age_from_birthdate3(2, 6, 2010)



''' 4. Recreate the previous function without the nested 
conditional, and using multiple condition on the first if. 
Use elif statements thereafter to funnel the user in the 
right branch.'''

def age_from_birthdate4(day, month, year):
    now = datetime.now()
    yeardiff = now.year - year
    monthdiff = now.month - month
    daydiff = now.day - day
    if monthdiff>0:
        age = yeardiff
    elif monthdiff<0:
        age = yeardiff-1
    elif daydiff>0:
        age = yeardiff
    elif daydiff<0:
        age = yeardiff-1
    else:
        print("Happy birthday!")
        age = yeardiff
    print(f"Your age is {age}")

age_from_birthdate4(13, 4, 1990)

age_from_birthdate4(20, 6, 1989)

age_from_birthdate4(1, 12, 1995)

age_from_birthdate4(2, 6, 2010)



''' 5. Create a game of head or tails where the user 
is asked to choose between heads or tails, and the scripts 
randomly generates either a 1 or a 0 and tells the player 
if they have won or lost. (for this you'll need the random 
library... see example). Your function should make use of 
booleans to test whether the user has won or not. '''

import random

def coinflip():
    guess = input("Please enter 'heads' or 'tails'")
    if guess in ["heads", "tails"]:
        flip = random.randint(0, 1)
        if flip==1:
            flip = "heads"
        if flip==0:
            flip = "tails"
        if guess==flip:
            print("Correct!")
        else:
            print("Incorrect!")
    else:
        print("Invalid guess")

coinflip()





