#找到最大的整數
def findMax(nums):
    list_length=len(nums)
    i=0
    max_num=nums[0]
    while list_length>0:
        if nums[i]>max_num:
            max_num=nums[i]
        i+=1
        list_length-=1
    return max_num
list1=[-5, -10, -8, 1, -1]
first_num=findSecond(list1)
print(first_num)