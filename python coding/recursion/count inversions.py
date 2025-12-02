def merge_sort_and_count(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Sort left and right halves and count inversions
    left_sorted, left_inv = merge_sort_and_count(left)
    right_sorted, right_inv = merge_sort_and_count(right)

    # Merge both halves and count cross inversions
    merged, cross_inv = merge_and_count(left_sorted, right_sorted)

    # Total inversions = left + right + cross
    total_inv = left_inv + right_inv + cross_inv
    return merged, total_inv


def merge_and_count(a, b):
    merged = []
    i = j = 0
    inv_count = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            inv_count += len(a) - i  # all remaining elements in a[] are > b[j]  ,  And because a is already sorted, all elements from a[i] to the end of a will also be greater than b[j]
            j += 1

    # Add remaining elements
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged, inv_count


# Example usage:
arr = [3, 2, 7, 1, 4, 5]
sorted_arr, inversion_count = merge_sort_and_count(arr)
print("Sorted array:", sorted_arr)
print("Total inversions:", inversion_count)
