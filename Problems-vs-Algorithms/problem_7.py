# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root

        split_path = path.split("/")

        for item in split_path:
            if item not in current_node.children:
                current_node.insert(item)
            current_node = current_node.children[item]
        current_node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root

        if path == "/":
            return current_node.handler
        
        split_path = path.split("/")

        if split_path[-1] == "":
            split_path = split_path[:-1]

        for item in split_path:
            if item not in current_node.children:
                return None
            current_node = current_node.children[item]
        return current_node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = dict()

    def insert(self, handler):
        # Insert the node as before
        if handler not in self.children:
            self.children[handler] = RouteTrieNode()

class Router:
    def __init__(self, handler, not_found_handler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.route_trie.insert(path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        handler = self.route_trie.find(path)

        if handler is None:
            return self.not_found_handler
        else:
            return handler

    def split_path(self):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        pass

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler","not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))
# 'root handler'
print(router.lookup("/home"))
# 'not found handler'
print(router.lookup("/home/about"))
# 'about handler'
print(router.lookup("/home/about/"))
# 'about handler'
print(router.lookup("/home/about/me"))
# 'not found handler'
