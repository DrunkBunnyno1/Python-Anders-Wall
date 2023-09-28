def fizz_buzz(input):
    
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"

    return input
    

print(fizz_buzz(7))

# /3 fizz
# /5 Buzz
# /5 and / 3 FizzBuzz
# !/ 3 or 5 return number


str = "33.2"
print(str)
print(float(str))








