nums = [1,1,2,4,4,5,7,8,9,0,1,1,2,3,5,4,4,4,5,6,5,8]
nums = sorted(nums)

i = 1
bound = len(nums)
prev = nums[0]
        
while i < bound:
    if prev == nums[i]:
        nums.pop(i)
        bound = len(nums)
    else:
        prev = nums[i]
        i += 1
print(len(nums))
print(nums)