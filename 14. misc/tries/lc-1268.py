class TrieNode:
    def __init__(self):
        self.children = {}  #Hashmap to contain children letters and their data
        self.suggestions = []   #List of suggestions
    
def makeTrie(words):
    root = TrieNode()

    for word in words:
        curr = root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]

            curr.suggestions.append(letter) #Insert the current word as suggestion
            curr.suggestions.sort() #Sorting the suggestions
            if len(curr.suggestions) > 3:
                curr.suggestions.pop()      #Remove the other suggestion to keep the lexicographically minimum ones
    
    return root

def getSuggestions(trie, searchWord):
    ans = []
    curr = trie
    for letter in searchWord:
        if letter in curr.children:
            curr = curr.children[letter]
            ans.append(curr.suggestions)
        else:
            return ans
    
    return ans
            


