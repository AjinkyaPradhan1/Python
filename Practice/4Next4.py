#Given a list of ints, return True if the array contains a 4 next to a 4 somewhere

def has44(x):
    for i in range(len(x)-1):
        if x[i:i+2]==[4,4]:
            return True
    return False
