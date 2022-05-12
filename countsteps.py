#counting number of cumputations with recursive function with 1 or 2 steps until n

def countsteps(n):
    
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return countsteps(n-2) + countsteps(n-1)
