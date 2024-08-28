nums = [0,1,0,1,0,1,99]

def containsDuplicate(nums) :
    if len(nums) == 1:
            return False        
    res = {}
    for e in nums :
        if e in res :
            return True
        else:
            res[e] = 1
    return False

print(containsDuplicate(nums))