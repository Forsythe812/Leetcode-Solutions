nums = [4,1,2,1,2]

def singleNumber(nums) :
    
    res = {}
    for i in nums :
        if i in res :
            del res[i]
        else : 
            res[i] = 1
    
    for k in res:
            return k
    
#     res = {}
#     for e in nums :
#         if e in res :
#             res[e] += 1
#         else:
#             res[e] = 1
#     for key,value in res.items() :
#         if 1 == value:
#             return key
print(singleNumber(nums))