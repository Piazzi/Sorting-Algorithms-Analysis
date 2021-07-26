import random
# Sorts array a[0..n-1] using Bogo sort
def bogoSort(arr):
    result = isSorted(arr)
    while (result == False):
        shuffle(arr)
        result = isSorted(arr)
    return result
 
# To check if array is sorted or not
def isSorted(arr):
    n = len(arr)
    count = 0
    for i in range(0, n - 1):
        count = count + 1
        if (arr[i] > arr[i+1] ):
            return False
    # if the array is sorted returns the number of comparisons made
    return count
 
# To generate permutation of the array
def shuffle(arr):
    n = len(arr)
    for i in range (0,n):
        r = random.randint(0,n-1)
        arr[i], arr[r] = arr[r], arr[i]