def partitionMedian(arr, low, high):
    i = low - 1
    j = high + 1
    med = (low + high) // 2
    pivot = arr[med]
    while True:
        while True:
            i += 1
            if arr[i] >= pivot:
                break
        while True:
            j-=1
            if arr[j] <= pivot:
                break
        if i >= j:
            return j
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    return i

def quickSort(arr, low, high):
    if low <  high :
        pi = partitionMedian(arr, low, high - 1)
        quickSort(arr, low, pi)
        quickSort(arr, pi+1, high)


#
# f = open('testFile_quickSort.txt', 'r')
# testFile = f.read().split('\n')

testFile = [190, 10, 5, 288, 8,4, 1, 0, 1, 4, 6,294, 7]

length = len(testFile)
quickSort(testFile, 0, length)
print(testFile)
