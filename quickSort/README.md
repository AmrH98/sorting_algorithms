# Sorting Algorithms Implementation

### QuickSort

- QuickSort is a Divide and Conquer algorithm.
 It picks an element as pivot and partitions the given 
 array around the picked pivot. There are many different 
 versions of quickSort that pick pivot in different ways.
 
#### Types

- Always pick first element as pivot.
- Always pick last element as pivot (implemented below)
 - Pick a random element as pivot.
 - Pick median as pivot.

 
#### Analysis of QuickSort
 - Time taken by QuickSort in general can be written as following.
 
        T(n) = T(k) + T(n-k-1) + \theta(n)
        
  ##### Worst Case: 
  - The worst case occurs when the partition process always picks greatest or smallest element as pivot. If we consider above partition strategy where last element is always picked as pivot, the worst case would occur when the array is already sorted in increasing or decreasing order. Following is recurrence for worst case.
   
        T(n) = T(0) + T(n-1) + \theta(n)
        which is equivalent to  
        T(n) = T(n-1) + \theta(n)
 ##### Best Case: 
 - The best case occurs when the partition process always picks the middle element as pivot. Following is recurrence for best case.
   
            T(n) = 2T(n/2) + \theta(n)
 ##### Average Case: 
 - Average time Complexity for Quicksort
 
        T(n) = T(n/9) + T(9n/10) + \theta(n)
 
 ##### Pseudocode
 
        Partition(A[],L,R) 
        {
            pivot = A[L]
            i = L
            for (j =L+1 to R+1 )
            {
                if (A[j] <= pivot)
                {
                    i++;    // increment index of smaller element
                    swap A[i] and A[j]
                }
            }
            swap A[i] and A[L])
            return (i)
        }
      
      