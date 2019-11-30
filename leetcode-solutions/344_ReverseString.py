def reverseString(s):
    i = 0
    j = len(s)-1
    while i >=0 and i < len(s)/2 :
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        i+=1
        j-=1

string = ["h","e","l","l","o"]
print("Before passing to function")
reverseString(string)
print("After passing to function")
print(string)