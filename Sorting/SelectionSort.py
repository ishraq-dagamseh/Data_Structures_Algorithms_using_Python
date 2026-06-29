def SelectionSort(list):

    n=len(list)
    for i in range(n):
        index_min=i
        for j in range(i,n):
            if list[j]< list[index_min]:
                index_min=j
        list[index_min],list[i]= list[i], list[index_min]     



l=[20,39,343,13,32,90]
print(l)

SelectionSort(l)

print("List after sorting is: ",l)