# Example 1: Function returning a tuple

def create_ranga():
    return "Ranga", 1981, "India"

ranga = create_ranga()

print("Tuple:", ranga)
print("Type:", type(ranga))


# Example 2: Tuple unpacking

name, year, country = ranga

print("Name:", name)
print("Year:", year)
print("Country:", country)


# Example 3: Accessing tuple elements

print("Tuple Length:", len(ranga))
print("First Element:", ranga[0])
print("Second Element:", ranga[1])
print("Third Element:", ranga[2])


# Example 4: Creating tuples

person = ("Ranga", 5, "India")

print("Person:", person)
print("Person Type:", type(person))


# Example 5: Swapping variables

x = 0
y = 1

print("Before Swap:", x, y)

x, y = y, x

print("After Swap:", x, y)


# Example 6: Single-element tuple

value1 = (0)
value2 = (0,)

print("Value1 Type:", type(value1))
print("Value2 Type:", type(value2))