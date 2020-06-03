
# Code by Jason Adams

# Day 3 exercises

''' 1.     Create a module with functions for (1) finding the 
highest number in a list, (2) finding the lowest number in a 
list, (3) finding the average of the numbers in a list, (4) 
subtracting an adjustable number to each item in a list without 
going into negative numbers (0 being the lowest the numbers can 
go), and (5) combining 2 lists of numbers into 1. In a different 
file, import that module and test your functions on the following 
lists: '''

import listmod_Jason

list1 = [13, 67, 57,  43,  26,  19,   9,  33,  59,  90,  20,  64,   6,  81,  51,  92,  17,   1,  29,  98,  49,  58,  87,  39,  74,  61,  70,  40,  80,  36,  48,  38,  77,  46,  50,  34,  53,  42,  84,  52,   4,  72,  73,  79,  65,   8,  93,  69,  54,  28,  16,  31,  11,  44,  41,  75,  56,   5,  78,  23,  62,  99,  32, 100,  85,  24,  35,  10,  76,  95,  60,  63]
list2 = [27, 787, 801, 956, 613, 355, 859, 496, 775, 963, 973, 928, 891,   1, 818, 717, 484, 966, 288, 587, 180, 737, 334, 601, 328, 939, 242, 551, 121, 560, 368, 240, 711, 694, 130, 453, 739, 102,   8, 825, 354, 715, 832, 908, 262,  77,  73, 151]

listmod_Jason.givemax(list1)
listmod_Jason.givemax(list2)

listmod_Jason.givemin(list1)
listmod_Jason.givemin(list2)

listmod_Jason.giveaverage(list1)
listmod_Jason.giveaverage(list2)

newlist1 = listmod_Jason.subtracttwenty(list1)
newlist2 = listmod_Jason.subtracttwenty(list2)

print(newlist1)
print(newlist2)

combinedlist = listmod_Jason.concatenatelists(list1, list2)

print(combinedlist)



''' 2. Create a command line utility that writes entries 
given by a user into a journal file. Entries should be 
dated as well as appended. Your journal app should also 
offer the option to print to console the latest "x" number 
of entries, as per the user's choice. '''

def journalwriter():
    from datetime import datetime
    filename = input("Name of file (end with '.txt'): \n")
    myfile = open(filename, 'a')
    entry = input("Journal entry: \n")
    time = str(datetime.now())
    myfile.write(time + "\n")
    myfile.write(entry + "\n")
    myfile.write("\n")
    myfile.close()

journalwriter()



''' 4. Create a magic 8-ball application that takes a question 
from the user and answers from a random list of predetermined 
answers. '''

def magic8ball():
    question = input("What is your question? \n")
    if question[-1]!="?":
        print("This is not a question!")
    else:
        import random
        answerlist = ["Not looking good", "Try again", "Definitely not", "Why would you ask that?", "Yikes...", "Good luck with that"]
        print(random.choice(answerlist))

magic8ball()



''' 5. Write a class called Rectangle that can create rectangles 
objects. Theses objects will need dimensions, colours, and names. 
You should include methods to calculate the area of the rectangle, 
as well as changing their names and colours. '''

class Rectangle:
    def __init__(self, name, length, width, colour):
        self.name = name
        self.length = length
        self.width = width
        self.colour = colour

    def area(self):
        area = self.length*self.width
        print(f"Area of {self.name}: {area}")

    def changename(self, newname):
        self.name = newname

    def changecolour(self, newcolour):
        self.colour = newcolour















