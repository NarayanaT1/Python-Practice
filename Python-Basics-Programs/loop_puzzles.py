# Example 1: For loop with step 2

for i in range(1, 11, 2):
    print(i, end=" ")

print("\n")


# Example 2: Reverse for loop

for i in range(11, 0, -1):
    print(i, end=" ")

print("\n")


# Example 3: While loop

i = 2

while i * i < 10:
    print(i, end=" ")
    i = i + 1

print("done")


# Example 4: Break statement

for i in range(1, 11):
    if i == 5:
        break
    print(i, end=" ")

print("done")


# Example 5: Break on odd number

for i in range(2, 11):
    if i % 2:
        break
    print(i, end=" ")

print("done")


# Example 6: Continue statement

for i in range(1, 11):
    if i % 2:
        continue
    print(i, end=" ")

print("done")


# Example 7: Continue using !=

for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i, end=" ")

print("done")