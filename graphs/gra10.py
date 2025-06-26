"""
127. Word Ladder
"""
from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        queue = deque()
        queue.append((beginWord, 1))

        while queue:
            curr_word, level = queue.popleft()
            if curr_word == endWord:
                return level
            
            for i in range(len(beginWord)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == curr_word[i]:
                        continue
                    new_word = curr_word[:i] + c + curr_word[i+1:]
                    if new_word in word_set:
                        queue.append((new_word, level+1))
                        word_set.remove(new_word)
        return 0



s= Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(s.ladderLength(beginWord, endWord, wordList))

"""
Time complexity = O(len(word_list) x len(new_word) x 26)
space complexity =queue  O(n) + set O(n) = O(2n) = O(n)
"""