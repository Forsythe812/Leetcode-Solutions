arr = [[1,1,0],[1,0,1],[0,0,0]]

print("\nBefore reversing")
print(arr)
for i in range(len(arr)):
    #for j in range(len(arr[i])):
    j = 0
    k = len(arr[i]) - 1
    while j < int(len(arr[i]))/2 and j >= 0:
        temp = arr[i][j]
        arr[i][j] = arr[i][k]
        arr[i][k] = temp
        j+=1
        k-=1
print("\nAfter reversing")
print(arr)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 1 :
            arr[i][j] = 0
        else :
            arr[i][j] = 1
print("\nAfter and inverting")
print(arr)