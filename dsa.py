# to create a linkedlist we need two things
# a node class
# a linkedlist class
# Node class represents the elements in a linked list
class Node:
    def __init__(self, data):
        self.data = data  # holds the data of the node
        self.ref = None  # reference to the next node in the list, None signifies the end of the list


# LinkedList class to create and manipulate linked lists
class LinkedList:
    def __init__(self):
        self.head = None  # head of the list, None signifies an empty list

    # Method to print the linked list
    def print_ll(self):
        if self.head is None:  # if list is empty
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:  # traverse the list
                print(n.data)  # print the data of the current node
                n = n.ref  # move to the next node

    # Method to add a node at the beginning of the list
    def add_begin(self, data):
        new_node = Node(data)  # create a new node
        new_node.ref = self.head  # new node points to the current head of the list
        self.head = new_node  # new node becomes the head of the list


linked_list = LinkedList()
linked_list.add_begin(10)
linked_list.add_begin(25)
linked_list.add_begin(40)
linked_list.add_begin(55)

linked_list.print_ll()


# The Nodee class represents the individual elements in a linked list.
class Nodee:
    # Each node has two components: data and a link to the next node.
    def __init__(self, data):
        self.data = data  # The data stored in the node.
        self.link = None  # The link to the next node, initially set to None.


# The LinkedL class provides methods for manipulating a linked list.
class LinkedL:
    # When a new linked list is created, it has no nodes, so the head is None.
    def __init__(self):
        self.head = None

    # The add method inserts a new node at the beginning of the list.
    def add(self, data):
        new_node1 = Nodee(data)  # Create a new node with the given data.
        new_node1.link = self.head  # The new node points to the current head of the list.
        self.head = new_node1  # The new node becomes the head of the list.

    # The print method prints out the data in all of the nodes in the list.
    def print(self):
        temp = self.head  # Start at the head of the list.
        while temp:  # Continue until temp is None, which signifies the end of the list.
            print(temp.data)  # Print the data of the current node.
            temp = temp.link  # Move to the next node in the list.


# Create a new linked list.
linked = LinkedL()

# Add some nodes to the list.
linked.add(67)
linked.add(90)
linked.add(45)
linked.add(9)

# Print the data in the list.
linked.print()



