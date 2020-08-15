def partitionFirst(arr, low, high):
    i = low
    pivot = arr[low]
    for j in range(low+1, high+1):
        if arr[j] <= pivot:
            i+=1
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp
    return (i) #divide and conquer split next subarray to two with i + 1 as half of array

def quickSort(arr, low, high):
    if low < high:
        pi = partitionFirst(arr, low, high)
        quickSort(arr, low, pi)
        quickSort(arr, pi+1, high)




f = open('testFile_quickSort.txt', 'r')
testFile = f.read().split('\n')

testFile = [10, 2, 5, 8, 1]

length = len(testFile)
quickSort(testFile, 0, length-1)
print(testFile)


