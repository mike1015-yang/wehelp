def checkPassword(s):
    # 你的程式碼
    a=['!','@','#','$','%']
    i=0
    b=[]
    if len(s)<8 or len(s)>16:
        return False 
    elif s.islower()==True or s.isupper()==True: #都是小寫或大寫
        return False
    elif s.isalnum()==True: #都是英文和數字
        return False
    else:
        while i<len(s):
            if s[i] not in a:
                b.append(s[i])
            i+=1
        strb="".join(b)
        if strb.isalnum()==False:
            return False
        else:
            if strb.isalpha()==True or strb.isdigit()==True:
                return False
            return True 
b=checkPassword('!@#%$sS1')
print(b)
