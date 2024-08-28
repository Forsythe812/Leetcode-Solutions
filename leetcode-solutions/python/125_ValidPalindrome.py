def isPalindrome(s):
    import re
    
    stripped = re.sub('[^A-Za-z0-9]+','',s).lower()
    
    if len(stripped) == 0 or len(stripped) == 1 :
        return True
    
    i = 0
    j = len(stripped) -1
    
    while (i < j) :
        if stripped[i] != stripped[j] :
            return False
        i += 1
        j -= 1
    return True
    
x = "A man, a plan, a canal: Panama"

print(isPalindrome(x))