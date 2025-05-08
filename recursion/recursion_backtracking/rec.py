"""
print rushi 4 times with recursion

"""

def rus(count):
    if count == 4:
        return
    print("Rushi")
    count +=1
    rus(count)

rus(count = 0)

"""
here we did head recursion
first we did job 
last we called function
next we will do tail recursion
"""