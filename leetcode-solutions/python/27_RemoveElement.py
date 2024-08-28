nums = [0,1,2,2,3,0,4,2]
val = 2

def removeElement(nums, val):
        i = 0
        bound = len(nums) 

        while i < bound :
            if nums[i] == val :
                nums.pop(i)
                bound = len(nums) 
            else :
                i += 1
        return len(nums)

print(removeElement(nums,val))
print(nums)