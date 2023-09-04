# Problem 1 and Solution.
# Ask the user to input a number and check if this number is positive, negative or zero and print it out.

"""
num1 = input("Type a number: ")
num1 = int(num1)
if num1 < 0:
    print(f"Ur number is a negativ number, ur number is {num1}")
elif num1 > 0:
    print(f"Ur number is a posetiv number, ur number is {num1}")
else:
    print(f"Ur number is zero, {num1}")
"""

# Problem 2 and Solution.
# ask the user to input two numbers and check which one is the smallest and print it out.
"""
num1 = input("Type a number: ")
num2 = input("Type a new number: ")
num1 = int(num1)
num2 = int(num2)
if num1 < num2:
    print(f"The first number u typte is a smaler number, the smaler number is {num1}")
elif num2 < num1:
    print(f"The secund numer u typed is the smaler number, the smaler number is {num2}")
else:
    print(f"I cant see witch is the smaler number ar the number equal? \nNumber 1 : {num1}, Number 2 : {num2}?????")
"""


# problem 3 and solution.
# Ask the user to input three angles and check if the triangle has a right angle.
# Your code should make sure that all three angles are valid and make up a triangle.

"""
angle1 = input("Lets chek if u have a right angle triangle! \nType the first angle: ")
angle2 = input("Type the second angle: ")
angle3 = input("And finaly type the therd angle: ")
angle1 = int(angle1)
angle2 = int(angle2)
angle3 = int(angle3)
total_angel = angle1 + angle2 + angle3
if total_angel == 180:
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("U have a right angle triangle.")
    else:
        print("U dont have a right angle triangle.")
else:
    print(f"Chek ur angels, a triangle have the angel sum of 180* ur triangel have a sum of {total_angel}*")
"""
# Problem 4 and solution.
# The information in the following table is stated in a medicine package. Also it is stated that for children weight is more important than age.
# ***
# Information To be put in the script: 
# Adults & adolescent over 40KG > 12y 1-2 pills 
# Children 26-40KG 7-12y 1/2-1pill 
# Children 15-25KG 3-7y 1/2 pill
# ******************************
# Let the user input an age and a weight, the program should recommend the number of pills for the user.

"""
age = input("We whil try to rekomend the righet doseged, Please input age of recipient: ")
weight = input("Please input the weight of the recipient in KG: ")
age = int(age)
weight = int(weight)

if age >= 3 and weight >= 15:
    if age >= 12 and weight >= 40:
        print("U can give the recipient 2 pills")
    elif weight >= 26 and age >= 7:
        if age >= 10 and weight >= 40:
            print("U can give the recipient 2 pills")
        elif age <= 10 and weight >= 40:
            print("U can give the recipient 1 pill, consoult a doktor")
        elif age >= 7 and weight <= 40:
            print("U can give the recipient 1 pill")
    elif weight >= 15 and age >= 3:
        if weight >= 40:
            print("CONTACKT A DOKTOR PLEASE!!!!!!!!")
        elif weight >= 30 and weight < 40:
            print("U can give the recipient 1 pill, consult a docktor.")
        elif weight >= 26 and weight < 30:
            print (" U can give the recipient 1/2 pill, if that dont work u can give 1/2 pill and consult a doktor.")
        elif weight >= 15 and weight <= 25:
            print("U can give recipient 1/2 pill")
else:
    print("U shuld consult a doktor i cant rekomend u to give medicine")
"""
# Problem 5 and Solution
# Let the user input a number. Check if the number is
# 1. even or odd
# 2. is divisible by 5
# 3. is divisble by 5 and odd

import math

"""
num1 = input("Enter a numbder. ")
num2  = int(num1)
if (num2 % 2) == 0:
    print("Then number is evan.\n ")
else:
    print("The number is odd!\n ")
if (num2 % 5) == 0:
    print("And divisible by 5. ")
else:
    print("The number is not divisible by 5.")
"""

#problem 6 and solution
# The maximum allowed luggage size for boarding an airplane is:
# 1. weight: 8kg
# 1. dimensions: 55x40x23cm (length x width x height)
# Let the user input weight, length, width and height of the luggage. The program should check if the luggage is allowed or not.

weight = int(input("Enter the luggage weighet in Kg:\n "))
length = int(input("The luggage length in Cm?:\n "))
width = int(input("The luggage width in Cm?:\n "))
height = int(input("The luggage height in Cm?:\n "))
weig = False # cahnge in If-satment line 126
leng = False # cahnge in If-satment line 129
widh = False # cahnge in If-satment line 132
heig = False # cahnge in If-satment line 135


if weight >= 1 and weight <= 8: # cheking i value weight is ok if not elif, line 144 or line 147
    weig = True
    print(f"Ur luggage weight is ok: {weight} kg")
    if length >= 1 and length <= 55: # cheking i length
        leng = True
        print(f"Ur luggage length is ok: {length} cm")
    if width >=1 and width <= 40: # cheking i value width
        widh = True
        print(f"Ur luggage width is ok: {width} cm")
    if height >= 1 and height <= 23: # cheking i value height
        heig = True
        print(f"Ur luggage height is ok: {height} cm")
    if leng == True and widh == True and heig == True: # Print if ale is true
        print(f"The following criteria have been mett: \n weighet: {weig}\n length: {leng}\n width: {widh}\n height: {heig}")
        print("U can bring ur luggage on the plane")
    if leng == False or widh == False or heig == False: # Print if one is false
        print(f"The following criteria not have been mett: \n weighet: {weig}\n length: {leng}\n width: {widh}\n height: {heig}")
        print("U can`t bring ur luggage on the plane")
elif weight < 1:
    print("U`r transporting helium on an arplane in ur luggage!!!!")
    print("Remove helium and try agen")
elif weight > 8:
    print("U hawe to remove items from ur luggage")
