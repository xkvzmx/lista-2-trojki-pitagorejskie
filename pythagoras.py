def find1(sum):
    """Find the Pythagorean triple.
    @param sum: the sum of the lengths of the sides in the triangle
    @return (found,a,b,c,k): information whether three has been found,
    side a, b, c & number of steps needed."""
    found = False
    k = 0
    for a in range(1, sum+1):
        for b in range(1, sum+1):
            for c in range(1, sum+1):
                k += 9
                if(a**2 + b**2 == c**2) and (a+b+c == sum):
                    found = True
                    return(found,a,b,c,k)
    if not found:
        return(found,None,None,None,k)

#############################################

def find2(sum):
    """Find the Pythagorean triple.
    @param sum: the sum of the lengths of the sides in the triangle
    @return (found,a,b,c,k): information whether three has been found,
    side a, b, c & number of steps needed."""
    found = False
    k = 0
    for a in range(1, sum//3):
        for b in range(a+1, sum//2):
            for c in range(b+1, sum//2):
                k += 9
                if(a**2 + b**2 == c**2) and (a+b+c == sum):
                    found = True
                    return(found,a,b,c,k)
    if not found:
        return(found,None,None,None,k)

#############################################

def find3(sum):
    """Find the Pythagorean triple.
    @param sum: the sum of the lengths of the sides in the triangle
    @return (found,a,b,c,k): information whether three has been found,
    side a, b, c & number of steps needed."""
    found = False
    k = 0
    for a in range(1,sum//3):
        for b in range(a+1,sum//2):
            k += 7
            c = sum - (a+b)
            if(a**2 + b**2 == c**2):
                found = True
                return(found,a,b,c,k)
    if not found:
        return(found,None,None,None,k)      


#############################################

from math import *
def find4(sum):
    """Find the Primary Pythagorean triple.
    @param sum: the sum of the lengths of the sides in the triangle
    @return (found,a,b,c,k): information whether three has been found,
    side a, b, c & number of steps needed."""
    found = False
    k = 0
    for b in range(1,sum+1):
        k += 21
        m = floor(sqrt((sum-b)/2))
        n = b/(2*m) if(m!=0) else sum
        a = int(m**2 - n**2)
        c = int(m**2 + n**2)
        if (m**2 == (sum-b)/2) and (a**2+b**2 == c**2) and a>0:
            found = True
            return(found,a,b,c,k)
    if not found:
        return(found,None,None,None,k)


#############################################

def find5(sum):
    """Find the Pythagorean triple.
    @param sum: the sum of the lengths of the sides in the triangle
    @return (found,a,b,c,k): information whether three has been found,
    side a, b, c & number of steps needed."""
    found = False
    k = 0
    for c in range(sum//3+1,sum//2):
        k += 7
        sqa_b = c**2 - sum**2 + 2*sum*c #6
        if sqa_b >= 0: #1
            k += 3
            a_b = floor(sqrt(sqa_b)) #1
            if (a_b**2 == sqa_b): #2
                k += 5
                b = int((sum - c + a_b)/2) #3
                a = int(sum - (b + c)) #2
                found = True
                return(found,a,b,c,k)
            
    if not found:
        return(found,None,None,None,k)