class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    output = LinkedList()
    union_set = set()

    node_1 = llist_1.head
    while node_1:
        if node_1.value not in union_set:
            union_set.add(node_1.value)
            output.append(node_1.value)
        node_1 = node_1.next
    
    node_2 = llist_2.head
    while node_2:
        if node_2.value not in union_set:
            union_set.add(node_2.value)
            output.append(node_2.value)
        node_2 = node_2.next
    
    return output

def intersection(llist_1, llist_2):
    output = LinkedList()
    intersection_set = set()

    node_1 = llist_1.head
    while node_1:
        if node_1.value not in intersection_set:
            intersection_set.add(node_1.value)
        node_1 = node_1.next
    
    node_2 = llist_2.head
    while node_2:
        if node_2.value in intersection_set:
            intersection_set.remove(node_2.value)
            output.append(node_2.value)
        node_2 = node_2.next
    
    return output

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 -> 
print (intersection(linked_list_1,linked_list_2))
# 6 -> 4 -> 21 -> 

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 
print (intersection(linked_list_3,linked_list_4))
# (Nothing)

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1,1,1,1,1,1,1]
element_2 = [1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
# 1 ->
print (intersection(linked_list_5,linked_list_6))
# 1 ->

# Test case 4

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [1,1,1,1,1,1,1]
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print (union(linked_list_7,linked_list_8))
# 1 ->
print (intersection(linked_list_7,linked_list_8))
# (Nothing)

# Test case 5

linked_list_9 = LinkedList()
linked_list_0 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_0.append(i)

print (union(linked_list_9,linked_list_0))
# (Nothing)
print (intersection(linked_list_9,linked_list_0))
# (Nothing)
