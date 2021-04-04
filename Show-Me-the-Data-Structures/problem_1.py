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
        return new_node

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
    
    def to_tail(self, node):

        if node.next == None:
            #print(f'Node({node.key},{node.value}) is Tail')
            pass
        elif self.head == node:
            self.head = self.head.next
            node.next.prev = None
            node.next = None
            node.prev = self.tail
            self.tail.next = node
            self.tail = self.tail.next
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.tail
            self.tail.next = node
            self.tail = self.tail.next
            self.tail.next = None

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
            node = self.dictionary[key]
            self.history.to_tail(self.dictionary[key])
            return self.dictionary[key].value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key not in self.dictionary:
            new_node = self.history.enqueue(key, value)
            self.dictionary[key] = new_node
            
            if self.history.num_elements > self.capacity:
                rm_key = self.history.dequeue()
                del self.dictionary[rm_key]
        elif key in self.dictionary:
            self.history.to_tail(self.dictionary[key])
        else:
            pass

    def __repr__(self):
        s = "\n==== Cache content ====\n"
        s += "Dictionary " + str(self.dictionary) + "\n"
        s += str(self.history) + "\n"
        return s

our_cache = LRU_Cache(5)

print("\n==== Test cases ====")
print("--- Get from empty ---")
print("our_cache.get(1):   {}".format(our_cache.get(1)))
# -1
print("our_cache.get(3):   {}".format(our_cache.get(3)))
# -1

print("\n--- Set and get ---")
print("our_cache.set(1,1): {}".format(our_cache.set(1,1)))
# None
print("our_cache.set(2,2): {}".format(our_cache.set(2,2)))
# None
print("our_cache.set(3,3): {}".format(our_cache.set(3,3)))
# None
print("our_cache.set(4,4): {}".format(our_cache.set(4,4)))
# None
print("our_cache.set(5,5): {}".format(our_cache.set(5,5)))
# None

print("our_cache.get(5):   {}".format(our_cache.get(5)))
# 5
print("our_cache.get(1):   {}".format(our_cache.get(1)))
# 1
print("our_cache.get(3):   {}".format(our_cache.get(3)))
# 3
print("our_cache.get(4):   {}".format(our_cache.get(4)))
# 4
print("our_cache.get(2):   {}".format(our_cache.get(2)))
# 2
print("our_cache.get(7):   {}".format(our_cache.get(7)))
# -1

print("\n--- Over capacity ---")
print("our_cache.set(6,6): {}".format(our_cache.set(6,6)))
# None
print("our_cache.set(7,7): {}".format(our_cache.set(7,7)))
# None
print("our_cache.set(8,8): {}".format(our_cache.set(8,8)))
# None

print("our_cache.get(1):   {}".format(our_cache.get(1)))
# -1
print("our_cache.get(2):   {}".format(our_cache.get(2)))
# 2
print("our_cache.get(3):   {}".format(our_cache.get(3)))
# -1
print("our_cache.get(4):   {}".format(our_cache.get(4)))
# 4
print("our_cache.get(5):   {}".format(our_cache.get(5)))
# -1
print("our_cache.get(6):   {}".format(our_cache.get(6)))
# 6
print("our_cache.get(7):   {}".format(our_cache.get(7)))
# 7
print("our_cache.get(8):   {}".format(our_cache.get(8)))
# 8

print("\n--- Set twice ---")
print("our_cache.set(6,6): {}".format(our_cache.set(6,6)))
# None
print("our_cache.set(1,1): {}".format(our_cache.set(1,1)))
# None
print("our_cache.set(2,2): {}".format(our_cache.set(2,2)))
# None
print("our_cache.set(3,3): {}".format(our_cache.set(3,3)))
# None
print("our_cache.get(7):   {}".format(our_cache.get(7)))
# -1
print("our_cache.get(6):   {}".format(our_cache.get(6)))
# 6
