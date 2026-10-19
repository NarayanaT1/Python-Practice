# Example 1: Correct indentation

i = 1

if i == 1:
    print("Value of i is 1")


# Example 2: If-else indentation

i = 3

if i == 3:
    print("Value of i is 3")
else:
    print("Value of i is not 3")


# Example 3: Nested if statements

number = 10

if number > 0:
    print("Number is positive")

    if number % 2 == 0:
        print("Number is even")


# Example 4: Indentation inside loops

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print("Number:", number)

    if number % 2 == 0:
        print("Even Number:", number)


# Example 5: Indentation inside functions

def greet(name):
    print("Hello", name)
    print("Welcome to Python")


greet("Python Developer")