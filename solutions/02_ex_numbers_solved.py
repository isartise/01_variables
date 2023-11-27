

# 1
# Sides of rectangle are given below
# Calculate the diagonal using Pythagorean theorem

a = 8
b = 13

# With additional variable as a help
square_c = a ** 2 + b ** 2
c = square_c ** 0.5

# All calculations in one line
one_line_c = (a ** 2 + b ** 2) ** 0.5


# 2
# Coordinates of two points are given below
# Calculate the distance between them (also using Pythagorean theorem)

A_x = 30
A_y = 150
B_x = 120
B_y = 100

distance = ((A_x - B_x) ** 2 + (A_y - B_y) ** 2) ** 0.5


# 3
# Using floating point numbers to handle money may be a bad idea
# Use variables bellow to calculate dollars and cents totals

dollars_1 = 14
cents_1 = 23
dollars_2 = 10
cents_2 = 50

dollars_total = dollars_1 + dollars_2
cents_total = cents_1 + cents_2

print(dollars_total, "dollars")
print(cents_total, "cents")


# 4
# Change values from exercise 3 to $14,23 and $10,99
# What changes? Try to fix it using only integers

dollars_1 = 14
cents_1 = 23
dollars_2 = 10
cents_2 = 99

dollars_total = dollars_1 + dollars_2
cents_total = cents_1 + cents_2

extra_dollar = cents_total // 100
dollars_total = dollars_total + extra_dollar

cents_total = cents_total % 100

print(dollars_total, "dollars")
print(cents_total, "cents")


# 5
# Change values from exercise 3 to $14,23 and $10,80
# What changes? What could be useful?

# We could use zero padding to display proper price - below is not enough for single digit cents!
print("$" + str(dollars_total) + "," + str(cents_total))
