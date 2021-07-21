def insertionSort(arr):
    count = 0
    n = len(arr)
    # Traverse through 1 to len(arr)
    for i in range(1, n):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                count = count + 2
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return count