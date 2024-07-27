#質數測試
def checkPrime(n):
    # 你的程式碼
    if n<=1:
        return False
    else:
        i=2
        while i<=n:
            if i==n:
                return True
                break
            else:
                if n%i==0:
                    return False
                    break
                else:
                    i+=1
a=checkPrime(75)
print(a)