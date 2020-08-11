def partitionLast(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
    temp = arr[i+1]
    arr[i+1] = arr[high]
    arr[high] = temp
    return (i + 1) #divide and conquer split next subarray to two with i + 1 as half of array

def quickSort(arr, low, high):
    if low < high:
        pi = partitionLast(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi+1, high)

array = [10, 7, 8, 9, 1, 5]

f = open('testFile_quickSort.txt', 'r')
testFile = f.read().split('\n')
length = len(testFile)
quickSort(testFile, 0, length-1)
print(testFile)


