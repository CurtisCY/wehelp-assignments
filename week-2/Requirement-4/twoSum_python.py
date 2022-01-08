def twoSum(nums, target):
    n = len(nums) #N = 4
    copyNums = nums.copy()
    #print(copyNums)

    for i in range(n): 
        for j in range(1,n): 
            sum = nums[0]+nums[j]
            firstValue = nums[0]
            secondValue = nums[j]
            #print(sum)
            if sum == target:
                #print("第一個索引", copyNums.index(firstValue))
                #print("第二個索引", copyNums.index(secondValue))
                result = sorted([copyNums.index(firstValue), copyNums.index(secondValue)])
        #print(nums)
        #print('COPY',copyNums)
        
        startValue = nums[0]

        for k in range(n-1): #搬移數字    
            nums[k] = nums[k+1]
            #print('startValue',startValue)
        nums[n-1]=startValue

    #print("最終結果", nums)
    return result

#Test Condition
result=twoSum([2,11,7,15],9)
#result=twoSum([2,11,7,15],26)
#result=twoSum([2,11,7,15],18)
#result=twoSum([2,11,7,15],22)
#result=twoSum([2,11,7,15],17)

print(result)