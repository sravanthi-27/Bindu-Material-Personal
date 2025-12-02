#| Step | `i` | Unsorted Part from `i` | Smallest Value | Swap with `arr[i]`       | Array after swap          |
#| ---- | --- | ---------------------- | -------------- | ------------------------ | ------------------------- |
#| 1    | 0   | \[29, 10, 14, 37, 13]  | 10             | Swap 29 and 10           | **\[10, 29, 14, 37, 13]** |
#| 2    | 1   | \[29, 14, 37, 13]      | 13             | Swap 29 and 13           | **\[10, 13, 14, 37, 29]** |
#| 3    | 2   | \[14, 37, 29]          | 14             | Already in correct place | **\[10, 13, 14, 37, 29]** |
#| 4    | 3   | \[37, 29]              | 29             | Swap 37 and 29           | **\[10, 13, 14, 29, 37]** |
#| 5    | 4   | \[37]                  | 37             | Already in correct place | **\[10, 13, 14, 29, 37]** |
#def find_min_element(arr):
#    min = -1
#    for i in range(len(arr)):
#        if arr[i]<min:
#            min = arr[i]
#    return min

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i 
        for j in range(i+1,len(arr)):
            if arr[j] <arr[min_index]:
                min_index = j  #getting minimum value from half sorted array
        if i!=min_index:
            arr[i] , arr[min_index] = arr[min_index] , arr[i]
arr = [3,1,2,5,7,4]
selection_sort(arr)
print(arr)