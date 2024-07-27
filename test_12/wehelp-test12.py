#找到目標數字所在的多個索引位置
def findIndexes(nums, target):
    list=[]
    for i in range(len(nums)):
        if nums[i]==target:
            list.append(i)
    return list
a=findIndex([3, 2, 1, 5, 10],1)
print(a)