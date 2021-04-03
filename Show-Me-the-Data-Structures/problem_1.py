class Container:

    def __init__(self, value):
        self.value = value
        self.age = 0

    def get_value(self):
        return self.value

    def get_age(self):
        return self.age

    def increase_age(self):
        self.age += 1

    def reset_age(self):
        self.age = 0

    def __repr__(self):
        return f'Container({self.value}, {self.age})'


class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.data_dict = dict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.data_dict:
            self.data_dict[key].increase_age()
            return key
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key not in self.data_dict and len(self.data_dict) < self.capacity:
            self.data_dict[key] = Container(value)
            self.data_dict[key].increase_age()
        elif key in self.data_dict:
            self.data_dict[key].increase_age()
        else:
            least_value = self._find_least()
            del self.data_dict[least_value]
            self.data_dict[key] = Container(value)
            self.data_dict[key].increase_age()

    def _find_least(self):
        least_val = -1
        lowest_age = -1
        for value in self.data_dict.values():
            if lowest_age < 0 or value.age < lowest_age:
                lowest_age = value.age
                least_val = value.value
        return value.value


print("----------------------")
our_cache = LRU_Cache(2)
print(our_cache.data_dict)

print("----------------------")
print("set(1,1)")
our_cache.set(1,1)
print(our_cache.data_dict)

print("----------------------")
print("set(2,2)")
our_cache.set(2,2)
print(our_cache.data_dict)

print("----------------------")
print("set(3,3)")
our_cache.set(3,3)
print(our_cache.data_dict)

print("----------------------")
print("set(2,2)")
our_cache.set(2,2)
print(our_cache.data_dict)

print("----------------------")
print("get(2)")
our_cache.get(2)
print(our_cache.data_dict)