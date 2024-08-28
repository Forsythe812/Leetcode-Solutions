nums = [1,2,2,1,1,3]
def singleNumber(nums):
    res = {}
    for e in nums :
        if e in res :
            res[e] += 1
        else:
            res[e] = 1
    for key,value in res.items() :
        if 1 == value:
            return key

print(singleNumber(nums))