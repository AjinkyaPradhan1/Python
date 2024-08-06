#You are given two numbers a and b. When a is raised to some power p, we get a number x. Now, you need to find what is the value of x that is closest to b.


def nearestLowerPower(a,b):
    for i in range(1,b):
        a = a**i
        
        if (a**i) > b:
            return a
    
print(nearestLowerPower(2,4))
