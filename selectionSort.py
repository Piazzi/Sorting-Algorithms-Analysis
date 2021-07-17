 
# Traverse through all array elements
def selectionSort(A):
    for i in range(len(A)):
        
        # Find the minimum element in remaining unsorted array
        minIdx = i
        for j in range(i+1, len(A)):
            if A[minIdx] > A[j]:
                minIdx = j
                
        # Swap the found minimum element with the first element       
        A[i], A[minIdx] = A[minIdx], A[i]