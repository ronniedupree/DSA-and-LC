# Create a Node class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at begin of LL
    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # Method to add a node at any index
    # Indexing starts from 0.
    def insert_at_index(self, data, index):
        if index == 0:
            self.insert_at_begin(data)

        position = 0
        current_node = self.head
        while current_node is not None and position + 1 is not index:
            position = position + 1
            current_node = current_node.next

        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    # Method to add a node at the end of LL
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    # Update node of a linked list at given position
    def update_node(self, val, index):
        current_node = self.head
        position = 0

        if position == index:
            current_node.data = val
        else:
            while current_node is not None and position != index:
                position = position + 1
                current_node = current_node.next

            if current_node is not None:
                current_node.data = val
            else:
                print("Index not present")

    # Method to remove first node of linked list
    def remove_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next

    # Method to remove last node of linked list
    def remove_last_node(self):

        if self.head is None:
            return

        current_node = self.head
        while current_node is not None and current_node.next.next is not None:
            current_node = current_node.next

        current_node.next = None

    # Method to remove at given index
    def remove_at_index(self, index):
        if self.head is None:
            return

        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while current_node is not None and position + 1 != index:
                position = position + 1
                current_node = current_node.next

            if current_node is not None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    # Method to remove a node from linked list
    def remove_node(self, data):
        current_node = self.head

        if current_node.data == data:
            self.remove_first_node()
            return

        while current_node is not None and current_node.next.data != data:
            current_node = current_node.next

        if current_node is None:
            return
        else:
            current_node.next = current_node.next.next

    # Print the size of linked list
    def size_of_ll(self):
        size = 0
        if self.head:
            current_node = self.head
            while current_node:
                size = size + 1
                current_node = current_node.next
            return size
        else:
            return 0

    # print method for the linked list
    def print_ll(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


# create a new linked list
llist = LinkedList()

# add nodes to the linked list
llist.insert_at_end('a')
llist.insert_at_end('b')
llist.insert_at_begin('c')
llist.insert_at_end('d')
llist.insert_at_index('g', 2)

# print the linked list
print("Node Data")
llist.print_ll()

# remove a nodes from the linked list
print("\nRemove First Node")
llist.remove_first_node()
print("Remove Last Node")
llist.remove_last_node()
print("Remove Node at Index 1")
llist.remove_at_index(1)

# print the linked list again
print("\nLinked list after removing a node:")
llist.print_ll()

print("\nUpdate node Value")
llist.update_node('z', 0)
llist.print_ll()

print("\nSize of linked list :", end=" ")
print(llist.size_of_ll())
