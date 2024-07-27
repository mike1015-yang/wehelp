#檢查字串是否以 https:// 開頭
#注意:設為s[0:8]是因為"https://"必須在開頭，如果沒有限制的話，"https://"出現在中間也會出現true
def checkHTTPS(s):
    if "https://" in s[0:8]: #s[0:8]:取出從位置0到位置8的「前一個位置」字元
        print("true")
    else:
        print("false")
url=input("輸入網址: ")
checkHTTPS(url.lower())      #lower():把字串全部換成小寫