

"""
Trie without extra data at each node
"""
def buildTrie(word):
    root = {}

    for word in words:
        curr = root
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
    
    return root

def doesTrieContain(trie, word):

    curr = trie
    for letter in word:
        if letter in curr:
            curr = curr[letter]
        else:
            return False

    return True


"""
Trie with extra data at each node
"""
#A TrieNode class is necessary only when we need to store some additional data at each node,
#otherwise we can just use a hashmap
class TrieNode:
    def __init__(self):
        self.data = None
        self.children = {}  #A hashmap of children, the hashmap is like "a":TrieNode()

def buildTrieWithData(words):
    root = TrieNode()   #Create the root node

    for word in words:
        currNode = root
        for letter in word:
            if letter not in currNode.children:
                letterNode = TrieNode()
                currNode.children[letter] = letterNode
            
            currNode = currNode.children[letter]
    
    print(root)

words = ["mobile","mouse","moneypot","monitor","mousepad"]
simpleTrie = buildTrie(words)
print(doesTrieContain(simpleTrie, "mobile"))
print(doesTrieContain(simpleTrie, "mobsle"))
