number = 5

if number < 0:
    number = number + 10
    number = number + 5

print(number)

# Puzzle 1: Nested if-else

m = 15

if m > 20:
    if m < 20:
        print("m>20")
    else:
        print("Who am I?")


# Puzzle 2: Two separate if statements

l = 15

if l < 20:
    print("l<20")

if l > 20:
    print("l>20")
else:
    print("Who am I?")


# Puzzle 3: if-elif-else

k = 15

if k > 20:
    print(1)
elif k > 10:
    print(2)
elif k < 20:
    print(3)
else:
    print(4)