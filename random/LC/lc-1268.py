from typing import List

class Node:
    def __init__(self):
        self.children = {}
        self.isword = False
        self.suggestions = []
    
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        parent = self.root
        for c in word:
            if c not in parent.children:
                parent.children[c] = Node()
            parent = parent.children[c]

            # create suggestions here
            sugg = parent.suggestions
            sugg.append(word)
            sugg.sort()
            parent.suggestions = sugg[:3]
            print(f"char: {c}, sugg: {parent.suggestions}")

        parent.isword = True

    def get_sugg(self, word):
        parent = self.root
        for c in word:
            if c not in parent.children:
                parent.children[c] = Node()
            parent = parent.children[c]

        return parent.suggestions

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        ans = []
        for prod in products:
            trie.insert(prod)
        
        for i in range(1, len(searchWord)):
            ans.append(trie.get_sugg(searchWord[:i]))
        
        return ans
    

sol = Solution()
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

print("\n\n~~~~~~~~~~")
print(sol.suggestedProducts(products, searchWord))