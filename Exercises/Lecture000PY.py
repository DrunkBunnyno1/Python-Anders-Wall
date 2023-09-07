import math

# problem 1 and solution
""" 
a)  A right angled triangle has the catheti: a = 3 and b = 4 length units.
    Compute the hypothenuse of the triangle. (*)
b)  A right angled triangle has hypothenuse c = 7.0 and a cathetus a = 5.0 length units.
    Compute the other cathetus and round to one decimal. (*)
"""

# a
a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print(f"\nThe hypothenuse is {c} length units\n")

# b
c = 7
a = 5
b = math.sqrt((c**2)-(a**2))
print(f"\nThe other cathetus is {round(b,1)} length units\n")
# print(f"{b:4}") more relevent solution

# Problem 2 and soliton

"""
A machine learning algorithm has been trained to predict whether or not it would rain the next day.
Out of 365 predictions, it got 300 correct, compute the accuracy of this model.
"""

a = 365
b = 300
c = (b / a) * 100
print(f"\nThe AI predicted the whether {round(c,1)} precent of the time\n")
# print(f"{c:1}")
# accury = 300 // 365

# Problem 3 and soliton

"""
A machine learning model has been trained to detect fire. Here is the result of its predictions:
Calculated the accuracy using the following formula: (TP + TN) / (TP + FP + FN + TN)
"""


tp = 2 # True Positive (TP)
fp = 2 # False Positive (FP)
fn = 11 # False Negative (FN)
tn = 985 # True Negative (TN)

result = (tp + tn) / (tp + fp + fn + tn)
print(f"The accuracy of this model is {result}\n")

# Problem 4 and solution

"""
Compute the slope "k" and the constant term "m" of this line using the points A:(4,4) and B:(0,1).
"""

y1 = 4
y2 = 1
x1 = 4
x2 = 0
k= (y1-y2) / (x1-x2)
print(k)
m = 4 - k*4
print(m)
print(f"\nk={k}, m={m}, so the equation for the slope is y = {k}*x + {m}\n")



# Problem 5 an solution

"""
The Euclideam distance between the points "P1" and "P2" is the length of a line between them. 
Let P1:(3,5) and P2:(-2,4) and compute the distance between them.
"""

# Sqrt(x2-x1)**2 + (y2-y1)**2

y1 = 5
y2 = 4
x1 = 3
x2 = -2

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f"\nThe distance is around {round(distance, 1)} length units\n")

# Problem 6 and Solution
"""
Calculate the distance between the points P1:(2,1,4) and P2:(3,1,0) 
"""
p = [2,1,4]
q = [3,1,0]
d = math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2 + (p[2]-q[2])**2)
print(f"\nThe distance is around {round(d,2)} l.u\n")




