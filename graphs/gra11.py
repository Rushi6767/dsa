"""
word ladder 2
"""
from typing import List
from collections import deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset = set(wordList)
        if endWord not in wordset:
            return []
        
        result = []
        queue = deque()
        queue.append([beginWord])

        while queue:
            level_size=len(queue)
            chosen_word = set()

            for _ in range(level_size):
                sequence = queue.popleft()
                last_word = sequence[-1]

                if last_word == endWord:
                    result.append(sequence)
                    continue

                for i in range(len(last_word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        if ch == last_word[i] :
                            continue

                        new_word = last_word[:i] + ch + last_word[i+1:]

                        if new_word in wordset:
                            new_seq = sequence + [new_word]
                            queue.append(new_seq)
                            chosen_word.add(new_word)

            for word in chosen_word:
                wordset.remove(word)

        return result
    

"""
Time Complexity  : O(N * L * 26 + P)
    - N is the number of words in wordList
    - L is the length of each word
    - 26 is the number of lowercase English letters
    - P is the number of shortest transformation sequences returned

Space Complexity : O(P * L + N)
    - P * L for storing all transformation paths in the result and queue
    - N for the word set and temporary storage
"""
