arr=[ [1,2,3],
    [4,5,6]]

n=len(arr)# length of raws
m=len(arr[0])# length of columns

#reachig to array elements
for i in range(n):
    for j in range(m):
       print(arr[i][j], end=' ')

    print()   

print(arr[1][2])# retrieve 6 