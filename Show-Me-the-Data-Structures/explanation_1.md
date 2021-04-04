# Reason
```dict``` type is used to make data access O(1). ```Queue``` is used to delete the least recently used emelent. A doubly linked list is used for the value of the ```dict``` to enable to update the queue element.

# Efficiency
Time complexity is O(1) for accessing the value of ```dict``` with no iteration.

Space efficiency is O(n) because data types of ```dict``` and ```HistoryQueue``` which is used to store the used history are linearly dependent on the data size.
