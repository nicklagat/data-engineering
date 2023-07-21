"""Functions"""
import time


# DRY --> DO NOT REPEAT YOURSELF
def hello_func():
    print('Hello function!')


def hello_world():
    return "Hello World, code new bie"


def sasa_func(greeting, name='You'):
    return f"{greeting},{name}"


print(sasa_func('Hi'))

hello_func()
hello_func()
hello_func()
hello_func()

hello_world()
print(hello_world())


def add(x, y):
    return (x ** 2) + y


print(add(10, 5))
print(add(6, 3))
test = add(10, 10)
print(test)


def has_duplicates(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False


test = has_duplicates([1, 2, 3, 4, 5, 5, 7, 8, 9, 1])
print(test)


# linear search
def find_target(arr, target):
    for tar in arr:
        if arr[tar] == target:
            return tar
    return -1


test = find_target([1, 2, 3, 45, 9, 7, 11, 3, 4], 3)
print(test)


class linkedListNode:
    def __int__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode


node1 = linkedListNode("3")
node2 = linkedListNode("5")

node1.nextNode = node2
