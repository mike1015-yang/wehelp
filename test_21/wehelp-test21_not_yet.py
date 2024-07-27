def findMaxZero(nums):
    # 你的程式碼
    max_zero=0
    temp_zero=0
    for i in nums:
        if i!=0:
            not_all_zero=nums
            break
    if not_all_zero!=0:
        for i in not_all_zero:
            if i==0 and :
                temp_zero+=1
            else:
                if temp_zero>=max_zero:
                    max_zero=temp_zero
                    temp_zero=0
    else:
        max_zero=len(nums) 
    return max_zero
a=findMaxZero([0, 0, 1, 0, 0, 0])
print(a)