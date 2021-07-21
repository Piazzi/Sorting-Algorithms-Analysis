# Traverse through all array elements
def selectionSort(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        
        # Find the minimum element in remaining unsorted array
        minIdx = i
        for j in range(i+1, n):
            if arr[minIdx] > arr[j]:
                minIdx = j
                count = count + 1
                
        # Swap the found minimum element with the first element       
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    return count