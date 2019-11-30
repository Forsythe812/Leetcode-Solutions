def firstUniqChar(s):
    if len(s) == 0 :
        return -1
        
    arr = []
    res = {}
    for e in s :
        if e in res :
            res[e] += 1
        else :
            res[e] = 1
            arr.append(e)
    for i in arr :
        if res[i] == 1 :
            return s.index(i)
    return -1
s = "leetcode"    
print(firstUniqChar(s))