def singleNonDuplicate(nums) :
    res = {}
    for n in nums :
        if n in res :
            res[n] -= 1
        else :
            res[n] = 1
    for key, value in res.items():
        if value == 1 :
            return key
        else :
             return None

nums = [1,1,22,3,3,4,4,8,8]
print(singleNonDuplicate(nums))