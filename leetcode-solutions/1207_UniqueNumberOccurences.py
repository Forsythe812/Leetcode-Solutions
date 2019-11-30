nums = [1,2,2,1,1,3]

def UniqueNumberOccurences(nums):
    res = {}
    for i in nums :
        if i in res :
            res[i] += 1
        else :
            res[i] = 1
        
    values = list(res.values())
    for i in range(0,len(values)) :
        for j in range(i+1,len(values)) :
            if values[i] == values[j] :
                return False
    return True

print(UniqueNumberOccurences(nums))