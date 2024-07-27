#找到最小公倍數
def findLCM(n1, n2):
    i=1
    if n1>n2:
        while i<=n2:
            if n1*i%n2==0:
                return n1*i
                break
            i+=1
    else:
        while i<=n1:
            if n2*i%n1==0:
                return n2*i
                break
            i+=1
LCM=findLCM(12,6)
print(LCM)