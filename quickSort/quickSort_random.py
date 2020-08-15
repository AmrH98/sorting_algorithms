import random
# def partitionMedian(arr, low, high):
#     i = low
#     med = (high) // 2
#     pivot = arr[med]
#     for j in range(low, high ):
#         if j == med:
#             continue
#         if arr[j] <= pivot:
#             temp = arr[j]
#             arr[j] = arr[i]
#             arr[i] = temp
#             i+=1
#     temp = arr[i]
#     arr[i] = arr[med]
#     arr[med] = temp
#     return i

def partitionRandom(arr, low, high):
    i = low
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i+=1
    temp = arr[high]
    arr[high] = arr[i]
    arr[i] = temp
    return i

def partitionPickRandom(arr, low, high):
    r = random.randint(low, high)
    temp = arr[r]
    arr[r] = arr[high]
    arr[high] = temp
    return partitionRandom(arr,low, high)

def quickSort(arr, low, high):
    if low <  high :
        pi = partitionPickRandom(arr, low, high - 1)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)



f = open('testFile_quickSort.txt', 'r')
testFile = f.read().split('\n')

# testFile = [190, 10, 5, 288, 8,4, 1, 0, 1, 4, 6,294, 7]

length = len(testFile)
quickSort(testFile, 0, length)
print(testFile)


