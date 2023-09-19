"""def input_int():
    while True:
        try:
            my_int = int(input("Input int: "))
        except ValueError:
            print("my_int is not int")
        else:
            break
    return my_int

x = input_int()
print(f"X = {x}")"""

def input_int(promt = ""):
    while True:
        try:
            return int(input(promt))
        except ValueError:
            print("my int is not an int")
        

age =input_int("input age: ")
length = input_int("Input length: ")
weight = input_int("input weight: ")
print(f"age = {age}, length = {length}, weight = {weight}")

