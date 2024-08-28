def reverseStr(s, k):
    i = 0
    j = k-1
    arr = [n for n in s]
    while i < len(s) :
        x = i
        y = min(j, len(s)-1)
        while x < y :
            temp = arr[x]
            arr[x] = arr[y]
            arr[y] = temp
            x += 1
            y -= 1
        i = i + k * 2
        j = j + k * 2
    return ''.join(arr)
s = "abcdefg"
k = 2
print(reverseStr(s,k))