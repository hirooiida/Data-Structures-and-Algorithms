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
            return -1
        else:
            rm_key = self.head.key
            self.head = self.head.next
            if self.head != None:
                self.head.prev = None
            self.num_elements -= 1
            return rm_key
    
    def to_tail(self, key):
        current_node = self.head

        if self.tail.key == key:
            return
        
        if self.head.key == key:
            self.head = self.head.next
            current_node.next.prev = None
            current_node.next = None
            current_node.prev = self.tail
            self.tail.next = current_node
            self.tail = self.tail.next
            return

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
        return

    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0

    def __repr__(self):
        s = ""
        if not self.is_empty():
            current_node = self.head
            while current_node:
                s += "Node({},{}) ".format(current_node.key,current_node.value)
                current_node = current_node.next
            return s + "\n<- older   newer ->"
        else:
            return s + "history is empty"

class LRU_Cache(object):

    def __init__(self, capacity):
        self.history = HistoryQueue()
        self.dictionary = dict()
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.dictionary:
            self.history.to_tail(key)
            return self.dictionary[key]
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key not in self.dictionary:
            self.dictionary[key] = value
            self.history.enqueue(key, value)

            if self.history.num_elements > self.capacity:
                rm_key = self.history.dequeue()
                del self.dictionary[rm_key]

    def __repr__(self):
        s = "Dictionary " + str(self.dictionary) + "\n"
        s += str(self.history) + "\n"
        return s

our_cache = LRU_Cache(5)

print("\n---- Test 1: Get from empty ----")
print("Pass" if (our_cache.get(1) == -1) else "Fail")
print("Pass" if (our_cache.get(3) == -1) else "Fail")

print("\n---- Test 2: Set and Get ----")
our_cache.set(1,1)
our_cache.set(2,2)
our_cache.set(3,3)

print("Pass" if (our_cache.get(3) == 3) else "Fail")
print("Pass" if (our_cache.get(1) == 1) else "Fail")
print("Pass" if (our_cache.get(2) == 2) else "Fail")
print("Pass" if (our_cache.get(4) == -1) else "Fail")

our_cache.set(4,4)
our_cache.set(5,5)
our_cache.set(6,6)
our_cache.set(7,7)

print("Pass" if (our_cache.get(3) == -1) else "Fail")
print("Pass" if (our_cache.get(1) == -1) else "Fail")
print("Pass" if (our_cache.get(4) == 4) else "Fail")
print("Pass" if (our_cache.get(5) == 5) else "Fail")
