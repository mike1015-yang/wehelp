#找到最大公因數
def findGCD(n1, n2):
    if n1>n2:
        i=n2
        while i>0:
            if n1%i==0 and n2%i==0:
                return i
                break
            i-=1
    else:
        i=n1
        while i>0:
            if n2%i==0 and n1%i==0:
                return i
                break
            i-=1
GCD=findGCD(12,6)
print(GCD)

