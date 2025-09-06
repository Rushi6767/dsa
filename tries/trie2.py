"""
complete string
"""

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

    def check_prefix(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]

def CompleteString(n, a):
    trie = Trie()
    for word in a:
        trie.insert(word)

    best_words = ""
    for word in a:
        if trie.check_prefix(word) == True:
            if len(word) > len(best_word) or (len(word) == len(best_word) and word < best_word):
                best_word = word

    return best_word if best_word != "" else "None"



"""
Time complexity :  O((N X L) + (N X L)) where N = nuber of words, L = average length
Space complexity : 
"""