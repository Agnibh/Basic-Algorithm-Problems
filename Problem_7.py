# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self,handler):
        self.handler=handler
        self.word=''
        self.children=dict()

    def insert(self, word, handler=''):
        self.children[word]=RouteTrieNode(handler)

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler, notFoundHandler=''):
        self.root=RouteTrieNode(handler)
        self.root.word='/'                                                 # represent the root node with '/'
        self.notFoundHandler=notFoundHandler

    def insert(self, path, handler=''):
        current_node=self.root

        for word in path[:-1]:
            if word not in current_node.children:
                current_node.insert(word,self.notFoundHandler)              # add only the last word in the path with handler, all other sub paths get error handler
                current_node.word=word
            current_node=current_node.children[word]

        current_node.insert(path[-1],handler)                               # dding handler to the full path
        current_node=current_node.children[path[-1]]
        current_node.word=path[-1]

    def find(self, path):

        current_node=self.root
        for word in path:
            if word not in current_node.children:
                return self.notFoundHandler
            current_node=current_node.children[word]
        return current_node.handler

# The Router class will wrap the Trie and handle

class Router:
    def __init__(self, rootHandler, notFoundHandler):
        self.trie=RouteTrie(rootHandler,notFoundHandler)
        self.handler=rootHandler
        self.notFoundHandler=notFoundHandler

    def add_handler(self, path, handler):
        path_list=self.split_path(path)
        self.trie.insert(path_list,handler)

    def lookup(self, path):
        path_list=self.split_path(path)
        if len(path)==0:
            return self.notFoundHandler
        return self.trie.find(path_list)

    def split_path(self, path):
        return path.replace("/", " ").split()


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output

print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

print(router.lookup(""))
