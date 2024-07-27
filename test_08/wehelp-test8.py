#計算等差數列的總和
def sumOfArithmeticSequence(min, max, differ):
    #方法一
    new_list=list(range(min,max+1,differ))     #產生一個首項為min，末項為max，公差為differ的等差數列
    n=(new_list[len(new_list)-1]-min)/differ+1 #項數:(末項-首項)/公差+1
    return (new_list[len(new_list)-1]+min)*n/2 #總和:(上底+下底)*高/2
    #方法二
    i=1
    new_max=0
    #找出末項
    while min+differ*i<=max:
        new_max=min+differ*i
        i+=1
    n=(new_max-min)/differ+1 #項數
    return (new_max+min)*n/2 #總和
a=sumOfArithmeticSequence(10, 23, 5)
print(a)