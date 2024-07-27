#整數陣列 / 列表中，兩兩相乘的最大值
def findMaxProduct(nums):
    length=len(nums)
    i=0
    n=1
    max_num=0
    while i!=length-1:
        while n<length:
            if i==0 & n==1:
                max_num=nums[i]*nums[n]
                n+=1
            else:
                if  max_num<nums[i]*nums[n]:
                    max_num=nums[i]*nums[n]
                n+=1
        i+=1
        n=i+1
    return max_num
MaxProduct=findMaxProduct([3,1,9,4,5])
print(MaxProduct)
        
