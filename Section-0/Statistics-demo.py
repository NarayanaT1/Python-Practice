import statistics

marks = [1, 6, 9, 23, 2]

print("Mean:", statistics.mean(marks))
print("Median:", statistics.median(marks))

marks = [1, 6, 9, 23, 2, 7]

print("Median:", statistics.median(marks))
print("Median High:", statistics.median_high(marks))
print("Median Low:", statistics.median_low(marks))
print("Variance:", statistics.variance(marks))