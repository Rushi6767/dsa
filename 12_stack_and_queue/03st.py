"""
Understanding deque
"""
from collections import deque

lst = deque([])
lst.append(10)
lst.append(20)
lst.append(30)

lst.appendleft(5)
lst.appendleft(2)
print(lst)

lst.pop()
lst.popleft()
print(lst)

"""
deque gives all operations in O(1)
"""