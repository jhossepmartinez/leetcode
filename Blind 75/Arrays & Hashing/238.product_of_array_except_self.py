def productExceptSelf(nums):
    for i in range(len(nums)):
        for n in nums:
            if n == nums[i]:
                continue
            elif 


nums = [1,2,3,4]

print(productExceptSelf(nums))
