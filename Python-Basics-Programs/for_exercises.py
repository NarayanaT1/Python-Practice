# Example 1: Check if a number is prime

def is_prime(number):

    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


print("Is 15 Prime:", is_prime(15))
print("Is 7 Prime:", is_prime(7))


# Example 2: Sum of numbers up to N

def sum_upto_n(number):

    sum = 0

    for i in range(1, number + 1):
        sum = sum + i

    return sum


print("Sum up to 6:", sum_upto_n(6))
print("Sum up to 10:", sum_upto_n(10))


# Example 3: Sum of divisors

def calculate_sum_of_divisors(number):

    sum = 0

    if number < 2:
        return sum

    for divisor in range(1, number + 1):
        if number % divisor == 0:
            sum = sum + divisor

    return sum


print("Sum of Divisors of 6:", calculate_sum_of_divisors(6))
print("Sum of Divisors of 15:", calculate_sum_of_divisors(15))


# Example 4: Print number triangle

def print_a_number_triangle(number):

    for j in range(1, number + 1):
        for i in range(1, j + 1):
            print(i, end=" ")
        print()


print("Number Triangle:")
print_a_number_triangle(6)