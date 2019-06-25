def partition(lst, low, high):
    pivot = lst[high]
    i = low - 1
    j = low
    while j < high:
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
        j += 1
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1


def quicksort(lst):
    def quickSortHelper(lst, low, high):
        print("low is: ", low, " high is: ", high)
        if low < high:
            pivot_ind= partition(lst, low, high)
            print("p ind is:, ", pivot_ind, " new lst is: ", lst)
            quickSortHelper(lst, low, pivot_ind-1)
            quickSortHelper(lst, pivot_ind+1, high)
    quickSortHelper(lst, 0, len(lst)-1)
    return lst

print(quicksort([5,3,1,8,6]))