
# Code by Jason Adams

# Module for Day 3 Exercise 1 functions

''' 1.     Create a module with functions for (1) finding the 
highest number in a list, (2) finding the lowest number in a 
list, (3) finding the average of the numbers in a list, (4) 
subtracting an adjustable number to each item in a list without 
going into negative numbers (0 being the lowest the numbers can 
go), and (5) combining 2 lists of numbers into 1. In a different 
file, import that module and test your functions on the following 
lists: '''

def givemax(list):
    max = list[0]
    for i in list:
        if i>max:
            max = i
    print(f"Maximum value: {max}")

def givemin(list):
    min = list[0]
    for i in list:
        if i<min:
            min = i
    print(f"Minimum value: {min}")

def giveaverage(list):
    average = 0
    for i in list:
        average += i
    average = average/len(list)
    print(f"List average: {average}")

def subtracttwenty(list):
    newlist = []
    for i in list:
        if i-20>0:
            newlist.append(i-20)
        else:
            newlist.append(0)
    return newlist

def concatenatelists(a, b):
    newlist = a
    for i in b:
        newlist.append(i)
    return newlist





