from collections import deque

class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        # 1. Put all words into a set for fast lookups
        wordSet = set(wordList)
        # If the endWord is not in our list, we can’t transform to it
        if endWord not in wordSet:
            return []

        result = []              # To store all shortest sequences
        queue = deque()          # BFS queue of paths (lists of words)
        queue.append([beginWord])  # Start with the path ["beginWord"]

        while len(queue) != 0:
            level_size = len(queue)
            chosen_words = set()  # Words we will remove after this layer

            # Process everything in the current layer
            for _ in range(level_size):
                sequence = queue.popleft()   # A path so far
                last_word = sequence[-1]      # The most recent word

                # If we already reached endWord, record this path
                if last_word == endWord:
                    result.append(sequence)
                    # Don’t continue expanding this path; it’s complete
                    continue

                # Try changing each letter of last_word
                for i in range(len(last_word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        # Skip if the letter is the same
                        if ch == last_word[i]:
                            continue
                        # Form a new word by replacing the i-th letter
                        new_word = last_word[:i] + ch + last_word[i + 1:]
                        # If this new word is in our set, it’s valid
                        if new_word in wordSet:
                            # Make a new path by appending new_word
                            new_seq = sequence + [new_word]
                            queue.append(new_seq)
                            # Mark new_word for removal after this layer
                            chosen_words.add(new_word)

            # Remove all words that were used in this layer
            for w in chosen_words:
                wordSet.remove(w)

        return result