def BinarySearch(list, value):
    l=0 #index for 1st element
    h=len(list)-1 #index for last element
    while l<=h:
        m=(l+h)//2# index for middle element
        if list[m]== value:
            return True
        elif list[m]> value:
            h= m-1
        else:
            l=m+1     
    return False

list=list(range(1,7))
print(list)
print(BinarySearch(list, 6))
