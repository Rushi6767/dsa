"""
dynamic programming
we are store values in lists,dict
this process called memoization
"""


import time

def mimo(n, d):
    if n == 0:
        return 0
    elif n in d:
        return d[n]
    else:
        d[n] =  mimo(n-1, d) + mimo(n-2, d)
        return d[n]
    
d= {0:1, 1:1}

start = time.time()    
print(mimo(36, d))
print(time.time() - start)

print(d)
