# Trie or prefix tree stores strings one letter per node, with its children as all the potential next letters from stored words
# Implement the Trie class:
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

# Solution: Each node is a dict with all its potential children
class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur:
                cur[i] = {}
            cur = cur[i]

        cur['*'] = ''

    def search(self, word: str) -> bool:
        cur = self.root
        for i in word:
            if i not in cur:
                return False
            cur = cur[i]
        
        return '*' in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in prefix:
            if i not in cur:
                return False
            cur = cur[i]
        return True
    
obj = Trie()
obj.insert('apple')
print(obj.search('apple'))
print(obj.search('app'))
print(obj.startsWith('app'))
obj.insert('app')
print(obj.search('app'))

