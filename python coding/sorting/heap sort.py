#max heap:heap is a binary tree every parent node is greater than or equal to its children node 
#min heap:less than or equal to
#heap sort is used for max more
#at each iteration larger nomes comes at starting position so we swap the first one with last one so that larger element comes at last and do the process again
def heapify(arr, n, i):
    # arr: array
    # n: size of the heap
    # i: index of the current root

    largest = i  # Assume the current index is the largest
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # If left child exists and is greater than current largest
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap root with largest
        heapify(arr, n, largest)  # Recursively heapify the affected subtree


def heap_sort(arr):
    n = len(arr)

    # Step 1: Build a max heap
    # Start from the last non-leaf node and move upwards
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        # Swap the current root (max) with the end element
        arr[0], arr[i] = arr[i], arr[0]

        # Call heapify on the reduced heap (excluding the last element)
        heapify(arr, i, 0)
arr = [4, 10, 3, 5, 1]
heap_sort(arr)
print(arr)