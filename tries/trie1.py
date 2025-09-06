"""
Tries implementation 2
"""
class Trienode:
    def __init__(self):
        self.children = {}
        self.prefix = 0
        self.count_word = 0


class Trie:
    def __init__(self):
        self.root = Trienode()

    # insert word into trie(you can insert 2 or more times here)
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trienode()
            node = node.children[ch]
            node.prefix += 1
        node.count_word += 1

    def start_with(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.prefix
    
    def count_word(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.count_word
    
    def erase(self,word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return
            node = node.children[ch]
            node.prefix -= 1
        node.count_word -= 1
            

trie = Trie()
trie.insert("apple")
trie.insert("apple")
trie.insert("apple")
trie.insert("vivo")
trie.insert("vivo")

print(trie.count_word("apple"))
# print(trie.count_word("vivo"))

# print(trie.start_with("vi"))

trie.erase("apple")
print(trie.count_word("apple"))

# print(trie.start_with("appl"))

"""
Time complexity : O(L) where L = average for each
Space complexity : O(n X L) where N = nuber of words, L = average length
"""