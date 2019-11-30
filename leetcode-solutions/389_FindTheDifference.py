def findTheDifference(s, t): 
    s = sorted(s)
    t = sorted(t)
        
    for i in range(0,len(s)) :
        if s[i] != t[i] :
            return t[i]
    return t[-1]

s1 = "abcd"
s2 = "abcde"
print(findTheDifference(s1,s2))