# Problem 7: Request Routing in a Web Server with a Trie
## Reason
Trie is an useful data structure for the router implementation that requires fast access and response thanks to the use of the dictionary data type. 

## Efficiency
Time complexity is O(n) for both ```add_handler``` and ```lookup```. The worst case is to visit the same length of path to check the key path existence. The space efficiency is O(n). The worst case is to keep n number paths which start with all different path.
