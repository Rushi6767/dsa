class Trienode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Trienode()

    # O(L)
    # insert word into trie
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trienode()
            node = node.children[ch]
        node.is_end = True

    # O(L)
    # search exact word
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end
    
    # O(L)    
    # search exact word
    def start_with(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True



trie = Trie()
trie.insert("apple")
print(trie.search("appl"))
print(trie.start_with("appl"))

"""
Time complexity : O(L) where L = average for each
Space complexity : O(n X L) where N = nuber of words, L = average length
"""