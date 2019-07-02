def insertionSort(lst):
    for i in range(1, len(lst)):
        curr = lst[i]
        j = i - 1
        while j >= 0 and curr < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = curr


arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 
for i in range(len(arr)): 
    print ("% d" % arr[i]) 