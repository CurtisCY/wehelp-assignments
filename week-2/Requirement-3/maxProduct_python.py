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

    if (nums[-2]*nums[-1]>nums[0]*nums[1]):
        print("排序結果", nums)
        print("兩數相乘最大值", nums[-2]*nums[-1])
    else:
        print("排序結果", nums)
        print("兩數相乘最大值", nums[0]*nums[1])


maxProduct([5,20,2,6]) #Get 120
maxProduct([10, -20, 0, 3]) #Get 30
maxProduct([-1, 2]) # Get -2
maxProduct([-1, 0, 2]) # Get 0
maxProduct([5,-1,-2,0]) # Get 2
maxProduct([-7,-1,-2,-10]) # Get 70