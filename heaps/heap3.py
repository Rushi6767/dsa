"""
check Minimum Heap
"""

def brut_checkMinHeap(heap):
    c = heap[0]
    n = len(heap)
    for i in range(1, n):
        if c > heap[i]:
            return False
    return True

# heap = [40,6,9,12,16,13,19,21]
# print(brut_checkMinHeap(heap))
"""
Time complexity: O(n)
Space complexity: O(1)
"""

def check_with_while(heap):
    n = len(heap)
    internal = n//2 -1

    while internal >= 0:
        left = 2 * internal + 1
        right = 2 * internal + 2

        if left < n :
            if heap[left] < heap[internal]:
                return False
        if right < n:
            if heap[right] < heap[internal]:
                return False
        internal -= 1
    return True
heap = [40,6,9,12,16,13,19,21]
print(check_with_while(heap))

def checkMinHeap(heap):
    n = len(heap)
    internal = n//2 -1

    for i in range(internal, -1, -1):
        
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n :
            if heap[left] < heap[i]:
                return False
        if right < n:
            if heap[right] < heap[i]:
                return False
    return True

# heap = [40,6,9,12,16,13,19,21]
# print(checkMinHeap(heap))

"""
Time complexity: O(n/2) == O(n)
Space complexity: O(1)
"""