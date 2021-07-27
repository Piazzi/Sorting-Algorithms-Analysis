import random
# Sorts array a[0..n-1] using Bogo sort
def bogoSort(arr):
    count = 0
    result, count = isSorted(arr)
    while (result == False):
        shuffle(arr)
        result, comparisons = isSorted(arr)
        count = count + comparisons
    return count
 
# To check if array is sorted or not
def isSorted(arr):
    n = len(arr)
    count = 0
    for i in range(0, n - 1):
        count = count + 1
        if (arr[i] > arr[i+1] ):
            return [False, count]
    return [True, count]
 
# To generate permutation of the array
def shuffle(arr):
    n = len(arr)
    for i in range (0,n):
        r = random.randint(0,n-1)
        arr[i], arr[r] = arr[r], arr[i]