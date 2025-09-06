"""
Count distinct substring
"""

def countDistinctSubstrings(s):
    n = len(s)
    substrings = set()

    # Generate all substrings
    for i in range(n):
        temp = ""
        for j in range(i, n):
            temp += s[j]
            substrings.add(temp)

    # +1 to include the empty substring
    return len(substrings) + 1

"""
Time complexity :  O(n ^ 2)
Space complexity : O(n^2) X n//2 == O(n ^3)
"""

# too much space complexity

class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_and_count(self, word):
        node = self.root
        count_new_nodes = 0
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
                count_new_nodes += 1
            node = node.children[ch]
        return count_new_nodes

def countDistinctSubstrings(s):
    trie = Trie()
    result = 0

    # Insert all suffixes
    for i in range(len(s)):
        suffix = s[i:]
        result += trie.insert_and_count(suffix)

    # +1 for empty substring
    return result + 1

"""
Time complexity :  O(n ^ 2)
Space complexity : O(n^2)
"""