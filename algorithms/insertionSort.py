def insertionSort(arr):
    count = 0
    n = len(arr)
    # Loop from the second element of the array until
    # the last element
    for i in range(1, n):
        # This is the element we want to position in its
        # correct place
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        count = count + 1
        while j >= 0 and key < arr[j] :
                count = count + 1
                # Shift the value one position to the left
                # and reposition j to point to the next element
                # (from right to left)
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return count