def maxProduct(nums):
    #print(nums)
    n = len(nums)
    #print(n)

    for i in range(n):
        #print("i= ",i)
        for j in range(0, n-i-1):
            #print("j= ",j)
            if nums[j] > nums[j+1]:
                valueTemp = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = valueTemp

    print("排序結果", nums)
    print("兩數相乘最大值", nums[-2]*nums[-1])

maxProduct([5,20,2,6])
maxProduct([10, -20, 0, 3])
maxProduct([-1, 2])
maxProduct([-1, 0, 2])