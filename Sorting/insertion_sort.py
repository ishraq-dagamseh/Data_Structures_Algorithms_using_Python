def insertion_sort(arr):
    n=len(arr)

    for i in range(n):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j], arr[j-1]
            j=j-1
            print(arr)



arr=[2,4,1,3,12,32,2]
print(arr)
insertion_sort(arr)
print(arr)            
