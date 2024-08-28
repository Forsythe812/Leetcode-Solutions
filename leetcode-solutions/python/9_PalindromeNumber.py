def isPalindrome(x):
    arr = [i for i in str(x)]
    if len(arr) == 1 or len(arr) == 0:
        return True
    i = 0
    j = len(arr)-1
    
    while (i < j) :
        if arr[i] != arr[j] :
            return False
        i += 1
        j -= 1
    return True

x = 12321

print(isPalindrome(x))