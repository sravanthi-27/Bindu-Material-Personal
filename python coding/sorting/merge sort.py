#Merge Sort is a Divide and Conquer algorithm.
#Divide the array into halves until each piece has one element.
#Conquer (merge) the pieces back together in sorted order.
#[5, 3, 8, 4, 2]
#
#→ Split into:     [5, 3, 8]     and     [4, 2]
#→ Split again:    [5] [3, 8]         [4] [2]
#→ Split again:        [3] [8]
#[5], [3], [8], [4], [2]
#Each element is now a list of one — so it's "sorted."
#Start merging:
#Merge [3] and [8] → [3, 8]
#Merge [5] and [3, 8] → compare elements → [3, 5, 8]
#Merge [4] and [2] → [2, 4]
#Now we have:
#
#Left:  [3, 5, 8]
#Right: [2, 4]
#Final merge:
#Compare 3 and 2 → pick 2
#Compare 3 and 4 → pick 3
#Pick 4
#Pick 5
#Pick 8
#[2, 3, 4, 5, 8]
def merge_sort(arr):
    if len(arr)<=1:
        return arr 
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge_two_sorted_arrays(left,right,arr)
def merge_two_sorted_arrays(a,b,arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0  # i → index for a; j → index for b; k → index for arr

    while i<len_a and j<len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1
    while i<len_a:
        arr[k] = a[i]
        i+=1
        k+=1
    while j<len_b:
        arr[k] = b[j]
        j+=1
        k+=1

nums = [3,2,7,1,4,5]
merge_sort(nums)
print(nums)