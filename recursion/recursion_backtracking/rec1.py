"""
print rushi 4 times with Tail Recursion(Backtracking)

Tail Recursion = Backtracking
first we called function
last we did job 
"""


def rus(count):
    if count == 4:
        return
    
    count += 1
    rus(count)
    print("Rushi")

rus(count=0)