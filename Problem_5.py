## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.char=None                          # represents the value stored in the node
        self.is_word=False
        self.child=dict()

    def insert(self, char):
        ## Add a child node in this Trie
        self.child[char]=TrieNode()

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root=TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node=self.root

        if len(current_node.child)==0:              # represent the root node by empty character
            current_node.char=''

        for char in word:
            if char not in current_node.child:
                current_node.insert(char)
                current_node.char=char
            current_node=current_node.child[char]
        current_node.is_word=True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        if prefix=='':
            return self.root

        current_node=self.root
        for char in prefix:
            if char not in current_node.child:
                return None
            current_node=current_node.child[char]
        return current_node

    def find_words(self,node,string):           # function to find all the words that start from the current node
        word_list=list()                        # to store the words
        sublist=list()

        if node.is_word==True:                  # if there is a word, then add it to the list
            word_list.append(string)

        for char,child_node in node.child.items():
            sublist=self.find_words(child_node,string+char)             # recursively go through all the children nodes and find the words
            for items in sublist:
                word_list.append(items)

        return word_list

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        current_node=self.find(suffix)
        word_list=self.find_words(current_node,'')
        return word_list


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

print(MyTrie.suffixes('an'))

print(MyTrie.suffixes(''))
