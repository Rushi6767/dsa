"""
multiplication with recursion:

if you confuse you can check
"pythontutor" website
"https://pythontutor.com/render.html#mode=display"
"""

# def mul(a,b):
#     if b == 1:
#         return a
#     else:
#         return a + mul(a, b-1)
    
# print(mul(4, 3))



import time

def mul(a,b):
    if b == 1:
        return a
    else:
        return a + mul(a, b-1)

start = time.time()
print(mul(200, 20))
print(time.time() - start)