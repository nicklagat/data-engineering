# Numeric data types
"""Integers and Floats"""

num = 3.14
print(type(num))

x = 10
y = -3
print(x)  # output is 10
print(y)  # output is 3

x1 = 10.980
y1 = -7.554

print(type(x1))
print(type(y1))

"""Arithmetic Operators"""
# arithmetic operations
x = 5
y = 2.1

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)  # floor division
print(x % y)
print(x ** y)

# incrementing values
num = 2
num *= 1
print(num)

print(round(3.911929, 1))
print(abs(-872))

"""Comparisons Operators"""
# they will return booleans : true or false

num_1 = 3
num_2 = 1
test = str(num_1)
print(type(test))
print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(num_1 < num_2)

# casting --converting
num_1 = '3'
num_2 = '4'
print(num_1 + num_2)

print(int(num_1) + int(num_2))

age = 13
print(type(age))

age_1 = 3.114
print(type(age_1))

age += 1
print(age)

age += 3
print(age)

new_age = [1, 2, 3, 4]

for new in new_age:
    new *= 2
    print(new)

print(abs(-5))
print(round(7.9942, 2))

# casting  --> converting a string to an integer
value = '5000'
value = int(value)
print(type(value))
