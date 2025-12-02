#Given the array [5, 2, 9, 1]:
#Insertion Sort:
#Start from index 1: 2 is less than 5 → insert before → [2, 5, 9, 1]
#9 is already in place
#1 is inserted at beginning → [1, 2, 5, 9]
def insertion_sort(arr):
    for i in range(1, len(arr)): #consider 1st one is already sorted
        j = i  #compare i with all sorted elements so j=i-1 and in while loop we compare the key with sorted elements

        while j > 0 and arr[j-1]>arr[j]: #loop stops when j =-1 means the least element is placed at index 0
            arr[j - 1],arr[j] = arr[j],arr[j-1]
            j -= 1


    return arr
nums = insertion_sort([5,2,9,1])
print(nums)

#efficiency for swapping
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr
