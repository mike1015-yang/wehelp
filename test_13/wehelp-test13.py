#翻轉一個字串
def reverseString(s):
    length=len(s)
    new_list=[]
    while length>0:
        new_list.append(s[length-1])
        length-=1
    return "".join(new_list) #把list變成字串
reversestring=reverseString("hello")
print(reversestring)