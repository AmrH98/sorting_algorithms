# merge to count inversions
def mergeSort(array,sortedArray,left,right):
    mid = (right // 2)
    inversionCount = 0

    if left < right:
        # count inversion left subarray
        inversionCount += mergeSort(array,sortedArray,left,mid)
        #  count inversion right subarray
        inversionCount += mergeSort(array,sortedArray,mid+1,right-1)
        # merge both sub arrays
        inversionCount += merge(array,left,sortedArray,mid,right)
    return inversionCount

def merge(array,left,sortedArray, mid,right):
    # indices or left, right and sorted subarray
    i = left
    j = mid + 1
    k = left
    # temp array
    inversionCount = 0

    while i <= mid or j <= right:
        # no inversion
        if array[i] <= array[j]:
            sortedArray[k] = array[i]
            i+=1
            k+=1
        else:
    # count inversion
            inversionCount+=1
            sortedArray[k] = array[j]
            j+=1
            k+=1
    while i <= mid:
        sortedArray[k] = array[i]
        k += 1
        i += 1

    # Copy the remaining elements of right subarray into temporary array
    while j <= right:
        sortedArray[k] = array[j]
        k += 1
        j += 1
    return inversionCount


# f = open('/Users/amr/Downloads/Coursera/Stanford-Algorithms/gitup/inversion/Test.txt', 'r')
# testFile = f.read().split('\n')
testFile = [1, 20, 6, 4, 5]

length = len(testFile)
sortedArray = [0]*(length)
inversions = mergeSort(testFile,sortedArray,0,length)
print("Value = ", inversions)




