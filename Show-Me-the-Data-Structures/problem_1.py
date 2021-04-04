class Node(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return f'Node({self.key},{self.value})'
    
    def __str__(self):
        return f'Node({self.key},{self.value})'

class HistoryQueue(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
    
    def enqueue(self, key, value):
        new_node = Node(key, value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        self.num_elements += 1

    def dequeue(self):
        if self.is_empty():
            print("There is nothing to dequeue")
        else:
            self.head = self.head.next
            if self.head != None:
                self.head.prev = None
            self.num_elements -= 1
    
    def to_tail(self, key):
        current_node = self.head
        while current_node:
            if current_node.key == key:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                current_node.prev = self.tail
                self.tail.next = current_node
                self.tail = self.tail.next
                self.tail.next = None
                break

            current_node = current_node.next

    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0

    def __repr__(self):
        s = "<- older   newer ->\n"
        if not self.is_empty():
            current_node = self.head
            while current_node:
                s += "Node({},{}) ".format(current_node.key,current_node.value)
                current_node = current_node.next
            return s
        else:
            return s + "history is empty"

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        pass

our_cache = LRU_Cache(5)

history = HistoryQueue()
history.enqueue(1,1)
print(history)

history.enqueue(2,2)
print(history)

history.dequeue()
print(history)

history.enqueue(3,3)
history.enqueue(4,4)
print(history)

history.to_tail(3)
print(history)

history.dequeue()
print(history)

history.dequeue()
print(history)

history.dequeue()
print(history)

history.dequeue()
