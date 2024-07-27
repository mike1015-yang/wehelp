#將數字用固定小數位數的格式輸出
def formatFloat(n):
    # 你的程式碼
    formatfloat='{:.2f}'.format(n) #format函式
    return str(formatfloat)
a=formatFloat(100.1)
print(a)