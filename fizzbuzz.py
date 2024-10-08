input_number = input("Pass the integer: ")

number = int(input_number)

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(f"{number} is not divided by 5 nor 3")