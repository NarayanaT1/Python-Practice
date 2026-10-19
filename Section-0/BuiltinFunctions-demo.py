# Example 1: Using built-in sum() function

numbers = [12, 34, 56]

print("Sum of Numbers:", sum(numbers))


# Example 2: Adding two numbers

number1 = 10
number2 = 20

total = number1 + number2

print("Total:", total)


# Example 3: Avoid using built-in function names

sum = number1 + number2

print("Sum Variable:", sum)


# Example 4: Restore built-in sum() function

del sum

print("Built-in Sum:", sum([12, 34, 56]))


# Example 5: Using a safe variable name

sum_ = number1 + number2

print("Sum Using Safe Variable:", sum_)