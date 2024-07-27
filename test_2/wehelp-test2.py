#檢查輸入的領取金額是否合乎規範
def checkMoney(n):
    if 100<=n<=100000 and n%100==0:
        return True 
    else:
        return False
money=checkMoney(int(input("輸入領取金額: ")))
print(money)