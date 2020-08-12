import timeit
# My initial code
start = timeit.default_timer()


def mergeSort(array):
    arrayLength = len(array)
    if arrayLength > 1:
        mid = arrayLength // 2
        left, inversionLeft = mergeSort(array[:-mid])
        right, inversionRight = mergeSort(array[-mid:])
        mergeArray, inversionMerge = merge(left, right)
        return mergeArray, inversionLeft + inversionRight + inversionMerge
    else:
        # when reaching base case of 1 element no inversion occurs
        return array,0

def merge(left, right):
    i, j, inversions = 0, 0, 0
    tempArray = []

    while i < len(left) and j < len(right):
        tempArray.extend([min(left[i], right[j])])
        if left[i] < right[j]:
            i+=1
        #     no inversion
        else:
            inversions+=1
            j+=1
    # insert item to end of array left side first then right ( left smaller than right checked )
    asdasd = left[i:]
    tempArray.extend(left[i:])
    aefsafa = right[j:]
    tempArray.extend(right[j:])

    return tempArray, inversions

# testFile = [1, 20, 6, 4, 5]
f = open('Test.txt', 'r')
testFile = f.read().split('\n')
x = mergeSort(testFile)

print("Inversions: ", x[1])

#Your statements here

stop = timeit.default_timer()

print('Time: ', stop - start)