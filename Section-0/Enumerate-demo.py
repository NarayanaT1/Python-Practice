# Example 1: Iterate through numbers
numbers = [1, 4, 6, 3, 4]

for number in numbers:
    print(number)

# Example 2: Iterate with index
for index, number in enumerate(numbers):
    print(f"{index} - {number}")

# Example 3: Iterate through vowels
values = list("aeiou")

for index, vowel in enumerate(values):
    print(f"{index} - {vowel}")