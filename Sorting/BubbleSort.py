def bubble_sort(arr):
    n=len(arr)
    permutation=True # to ensure if we need to swap or not
    while permutation:
        permutation=False
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]= arr[i+1], arr[i]
                permutation=True


arr=[10,2,32,12,3]
print(arr)

bubble_sort(arr)
print(arr)