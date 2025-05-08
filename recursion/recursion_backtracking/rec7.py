"""
fibonnaci number by recursion
"""

def fibbo(n):
    if n==0 or n==1:
        return n
    else:
        return fibbo(n-1) + fibbo(n-2)
    
print(fibbo(6))