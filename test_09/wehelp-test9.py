#用預設值填滿空字串
def fill(words, value):
    i=0
    while i<len(words):
        if words[i]=='':
            words[i]=value
        i+=1
    return words
a=fill(["Hello", "World", ""],'test')
print(a)    