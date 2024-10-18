
def digitsCount(number):
    digits=1
    divisor=10
    while(True):
        if(number//divisor>0):
            digits=digits+1
            divisor=divisor*10
        else:
            return digits


def isPalindrome(digits,number):
    d=digits
    n=number
    i=0
    repeticiones=d//2
    while(i<repeticiones):
        i+=1
        a=n//(10**(d-1))
        b=n%10
        n = (n % (10**(d-1))) // 10
        d=d-2
        if a!=b:
            return False
    return True


p1=12345
p2=2552
p3=9812332189


print( isPalindrome(digitsCount(p1),p1) )
print( isPalindrome(digitsCount(p2),p2) )
print( isPalindrome(digitsCount(p3),p3) )
