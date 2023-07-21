"""List, Tuples and Sets"""

# a list is an ordered collection of items that are mutable (changeable)
# comma separated

list1 = [-9, 1, 2, 3, 4]

b_list = [x for x in list1]
print(b_list)

nu = []

for numb in range(1, (len(list1) + 1)):
    if numb not in list1:
        print(numb)

print("""New Page Skip""")
list2 = ['apple', 'banana', 'cherry']
list3 = [1, 'apple', 2.5, True]

print(min(list1))

print(list1)
print(list2)
print(list3)

courses = ['Maths', 'Physics', 'Biology', 'Chemistry', 'Software Engineering']
print(courses)
print(courses[1])
print(len(courses))
print(courses[4])
print(courses[-2])
print(courses[0:3])  # ['Maths', 'Physics', 'Biology']

courses.append('Art')
courses.insert(0, 'Quantum')

courses_2 = ['Space', 'DevOps']
courses.extend(courses_2)

courses.remove('Art')

popped = courses_2.pop()
print(popped)

print(courses)

nums = [1, 2, 3, 9, 7, 5, 0]
te = sorted(nums)
print(te)

print(min(nums))
print(sum(nums))
print(max(nums))

print(nums.index(3))
print('Maths' in courses)

for index, item in enumerate(courses):
    print(index, item)

# tuples are immutable
tuple1 = (1, 2, 4)
print(tuple1)

# sets are mutable
set1 = {1, 5, 7, 4}
set1.add("test")
print(set1)

nike_sneakers = ['Test']
print(nike_sneakers)

# a list of courses

courses = ['Maths', 'Biology', 'Physics', 'Chemistry', 'History']

for index, course in enumerate(courses):
    print(index, course)

print(len(courses))
print(courses[1])
print(courses[:3])
print(courses[2:])
print(courses[-1])
print(courses[-4:-1])
print(courses[-1:-4])
courses.append('Art')
print(courses)
courses.insert(2, 'Economics')
print(courses)

print(courses.sort())

numero_uno = [5, 4, 3, 1, 9, 6]
test = numero_uno.sort(reverse=True)
print(test)
print(numero_uno)

# find an index of a value in a list
print(numero_uno.index(4))
