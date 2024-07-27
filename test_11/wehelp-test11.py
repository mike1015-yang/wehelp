#找到目標數字所在的索引位置
def findIndex(nums, target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
            break
    return -1
a=findIndex([3, 2, 1, 5, 10],1)
print(a)
