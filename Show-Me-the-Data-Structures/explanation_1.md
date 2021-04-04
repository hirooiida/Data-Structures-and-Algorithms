# Reason
```dict``` data type is used for cache content to get ```get()``` function in O(n) efficiency.

Queue is used for cache history to remove the least recently used node when the capacity is full. The queue should be capable to update the order of its elements, a doubly linked list is used for the node and a function (```to_tail()```) is added as a member function.

# Efficiency
Time efficiency: O(n)

Space efficiency: O(n)

```to_tail(key)``` function requires ```n-2``` steps in the worst case if the node with the key is at just before the ```tail```, which makes time efficiency O(n). 