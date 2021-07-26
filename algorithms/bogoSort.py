import random

# Sorts array a[0..n-1] using Bogo sort
def bogoSort(arr):
    count = 0
    while (is_sorted(arr, count) == False):
        shuffle(arr)
    return count
 
# To check if array is sorted or not
def is_sorted(arr, count):
    n = len(arr)
    for i in range(0, n - 1):
        count = count + 1
        if (arr[i] > arr[i+1] ):
            return False
    return True
 
# To generate permutation of the array
def shuffle(arr):
    n = len(arr)
    for i in range (0,n):
        r = random.randint(0,n-1)
        arr[i], arr[r] = arr[r], arr[i]