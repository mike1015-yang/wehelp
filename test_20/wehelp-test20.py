#檢查是否為等差數列
def checkArithmeticSequence(nums):
    # 你的程式碼
    com_dif=nums[1]-nums[0]
    i=1
    while i<len(nums)-1:
        if nums[i+1]-nums[i] !=com_dif:
            return False
            break
        else:
            i+=1
    return True
a=checkArithmeticSequence([1, 3, 6])
print(a)