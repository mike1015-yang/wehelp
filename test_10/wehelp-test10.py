#用前一個有效值填滿空字串
def ffill(words):
    # 你的程式碼
    i=0
    while i<len(words):
        if words[i]=='':
            if words[i-1]!='' and i!=0:
                words[i]=words[i-1]
        i+=1
    return words
a=ffill(["", "a", "", "", "c"])
print(a)