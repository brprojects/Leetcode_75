# You are given an array of strings products and a string searchWord.
# Design a system that suggests at most three product names from products after each character of searchWord is typed. 
# Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix 
# return the three lexicographically minimums products.
# Return a list of lists of the suggested products after each character of searchWord is typed.

# Solution: Implement Trie with a list to store lexicographically minimum words for each prefix. Sort products initially so
# alphabetically lowest 3 products are added to list.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []
        self.n = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
            if node.n < 3:
                node.words.append(word)
                node.n += 1

    def startsWith(self, prefix: str):
        node = self.root
        for i in prefix:
            if i not in node.children:
                return ''
            node = node.children[i]
        return node.words


def suggestedProducts(products: list[str], searchWord: str) -> list[list[str]]:
    products.sort()
    trie = Trie()
    for word in products:
        trie.insert(word)
    ans, cur = [], ''
    for i in searchWord:
        cur += i
        ans.append(trie.startsWith(cur))
    return ans
    
print(suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))