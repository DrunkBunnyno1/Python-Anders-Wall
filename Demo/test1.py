

students = [
    {"name": "adam", "class": "AI23", "email": "adam@gmail.com"},
    {"name": "kalle", "class": "AI23", "email": "kalle@gmail.com"},
    {"name": "eva", "class": "AI22", "email": "eva@hotmail.com"},
]
for i in students:
    print(i)

with open("test\students.csv", "w") as file:
    for student in students:
        file.write(f"{student['name']}, {student['class']}, {student['email']}\n")
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
