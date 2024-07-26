def peak(nums):
    first = None
    second = None
    for i in range(len(nums)):
        first = nums[i]
        second = nums[i+1]
        if (second < first):
            return i
    
print(peak([0,10,5,2]))