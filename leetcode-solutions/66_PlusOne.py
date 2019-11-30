nums = [4,3,2,1]

def PlusOne (digits) :  
    r = int("".join(map(str, digits)))   
    r = r + 1
    listed = [int(x) for x in str(r)]
    return listed

print(PlusOne(nums))