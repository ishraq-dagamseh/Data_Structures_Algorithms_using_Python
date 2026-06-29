def Merge_Two_lists(list1, list2):
    n=len(list1)
    m=len(list2)
    i=0#index for first element in list1
    j=0#index for first element in list1
    result=[]
    while i<n and j<m:
        if list1[i]< list2[j]:
            result.append(list1[i])
            i+=1
        else:
            result.append(list2[j])
            j+=1    
    while i<n:
        result.append(list1[i])
        i+=1

    while j<m:
        result.append(list2[j])
        j+=1    
    return result


def merge_sort(arr):
    n=len(arr)
    if n<=1:
        return arr
    mid=n//2

    a=merge_sort(arr[0: mid])
    b=merge_sort(arr[mid: n])
    r=Merge_Two_lists(a, b)
    return r
arr=[2,41,1,3,1,5,2,62,2]
print(merge_sort(arr))
