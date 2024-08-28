
def intersect(nums1, nums2):
    res1 = {}
    ans = []

    for i in nums1 :
        if i in res1 :
            res1[i] += 1
        else :
            res1[i] = 1

    for j in nums2 :
        if j not in res1 or res1[j]==0 :
            continue
        else :
            res1[j]-=1
            ans.append(j)
        
    return ans

num1 = [1,2,2,1] 
num2 = [2,2]
print(intersect(num1,num2))