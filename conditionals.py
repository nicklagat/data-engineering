language = 'Javascript'

if language == 'Python':
    print("The state was True")

elif language == 'Javascript':
    print("Language is Javascript")

else:
    print("There's no match")

user = 'Adm'
logged_in = True

if user == 'Admin' and logged_in:
    print('Logged in using correct credentials')
elif user == 'System' and logged_in:
    print('Logged in as a system user')
else:
    print('Incorrect credentials')

a = [1,2,3]
c = a
b = [1,2,3]

print(id(a))
print(id(c))
print(id(b))
print(a is c)