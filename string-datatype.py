# Python Datatypes
eat_food = 'test'
print(eat_food)

message = 'Hello, World!'
print(message)

holiday_message = "Good morning, everyone?, How's work so far?"
print(holiday_message)

# Multi-line quotes
message_again = """
Hey there
"""

print(message_again)

# Length
print(len(message))

# Slicing
print(message[:3])

# String methods
print(holiday_message.lower())
print(holiday_message.upper())
print(len(holiday_message))
print(holiday_message.find('far'))

new_message = message.replace('World', 'Worlder')
print(new_message)

greeting = 'Hey'
name = 'Michael'

message = greeting + ', ' + name
print(message)

# Formatted string
message = '{}, {}. Welcome!'.format(greeting, name)
message_1 = f'{greeting}, {name}. Welcome!'
print(message)
print(message_1)
# print(dir(message))
# print(help(str))

# Concatenation
string_one = 'Hello'
string_two = 'World!'
print(string_one * 3)

# String formatter
print(f'{string_one} {string_two}')
print('{} {}'.format(string_one, string_two))

# Indexing and slicing
str1 = 'Hey World'
print(str1[0])
print(str1[4])
print(str1[0:5])

# String methods
str1 = 'Hello, World!!'
print(str1.upper())
print(str1.lower())
print(str1.find('World'))
print(str1.replace('World', 'Python'))
print(str1.isdigit())

# String formatting
str1 = 'World'
# Using str1.format()
print("Hello, {}!".format(str1))
# Using f-string
print(f'Hello, {str1}!')

age = 45
print(f'You are {age} years old!!')

tourist = "Visit Croatia"
print(tourist)
new_tourist = tourist.replace("Croatia","Berlin")
print(new_tourist)

say = 'Hi'
namesta = 'Nick'
print(f'{say},{namesta}')
print('{},{}'.format(say,namesta))

#
# print(dir(say))
# print(help(str))

scores = []
print(len(scores))
scores.append('Lesson')
print(scores)

