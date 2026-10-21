# Example 1: Print squares up to a limit

def print_squares_upto_limit(limit):
    i = 1

    while i * i < limit:
        print(i * i, end=" ")
        i = i + 1


# Example 2: Print cubes up to a limit

def print_cubes_upto_limit(limit):
    i = 1

    while i * i * i < limit:
        print(i * i * i, end=" ")
        i = i + 1


# Execute both functions

print("Squares up to 30:")
print_squares_upto_limit(30)

print("\n")

print("Cubes up to 30:")
print_cubes_upto_limit(30)

print("\n")

print("Cubes up to 80:")
print_cubes_upto_limit(80)