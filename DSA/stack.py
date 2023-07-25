# implementing stack data structure using a list

# pushing elements to the stack
stack = []
stack.append(10)
stack.append(9)
stack.append(200)

print(stack)

# popping elements from the stack
stack.pop()
stack.pop()
stack.pop()

print(stack)

# checking if the stack is empty
print(len(stack) == 0)

# empty stack
stack = []


def append():
    element = input('Add your element to the stack: ')
    stack.append(element)
    print(stack)
    return stack


def pop():
    if not stack:
        print('Stack is empty')
    else:
        e = stack.pop()
        print(f'Removed element is: {e}')
        print(stack)


while True:
    print("Select your operations 1.append, 2.pop, 3.quit")
    choice = int(input(""))
    if choice == 1:
        append()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("Enter correct operation")


