# # input list
# inputList = [45, 150, 20, 90, 15, 55, 12, 75]
# # Printing the given list
# print("The Given list is:", inputList)
# # input value
# inputValue = 50
# # iterarting through the list
# for i in inputList:
#    # checking whether the current element is greater than the input value
#    if i < inputValue:
#       # removing that current element from the list if the condition is true
#       inputList.remove(i)
# # printing the resultant list after removing elements larger than 50
# print("Removing elements larger than 50 from the list:\n", inputList)


my_list = [100000,1000009,10000001,1000002,1000003,1000004,1000005,1000006,1000007,1000008]
cont = 0
for number in range(20):
    x = 1 + 1
    for i in my_list:
        cont += 1
        if i > x:
            z = i
            print(x)
            print(i)
            print(z)
            my_list.remove[i]
            #my_list.append(x)
        elif x > i:
            x = x
print(my_list)


# students = [
#     {"name": "adam", "class": "AI23", "email": "adam@gmail.com"},
#     {"name": "kalle", "class": "AI23", "email": "kalle@gmail.com"},
#     {"name": "eva", "class": "AI22", "email": "eva@hotmail.com"},
# ]
# for i in students:
#     print(i)

# with open("test\students.csv", "w") as file:
#     for student in students:
#         file.write(f"{student['name']}, {student['class']}, {student['email']}\n")
#
#import csv
#
#students = []
#
#with open("..\\data\\students.csv") as file:
#    reader = csv.DictReader(file)
#
#    for row in reader:
#        #print(row["name"])
#        students.append({"name": row["name"], "class": row["class"], "email": row["email"]})
#
#print(students)"""
