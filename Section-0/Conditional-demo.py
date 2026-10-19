# Example 1: Traditional if-else condition

number = 5

if number % 2 == 0:
    isEven = True
else:
    isEven = False

print("Is Even:", isEven)


# Example 2: Using conditional expression

number = 6

isEven = True if number % 2 == 0 else False

print("Is Even:", isEven)


# Example 3: Simplified Boolean expression

isEven = number % 2 == 0

print("Is Even:", isEven)


# Example 4: Conditional expression returning strings

isEven = "Yes" if number % 2 == 0 else "No"

print("Is Even:", isEven)