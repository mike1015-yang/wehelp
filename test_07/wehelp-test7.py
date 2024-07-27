#將整數陣列 / 列表，轉換為逗號隔開的字串
def toCSVString(nums):
    length=len(nums)
    i=0
    nem_str=''
    if length==0: #空字串的長度為0，比較好用在判斷式
        return ''
    else:
        while length>0:
            if i==len(nums)-1:
                return new_str+str(nums[i])
            else:
                new_str=new_str+str(nums[i])+','
            i+=1
            length-=1
CSVString=toCSVString([])
print(CSVString)