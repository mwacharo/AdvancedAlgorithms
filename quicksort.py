def quick_sort(arr):
    """Recursively sorts an array using Quick Sort algorithm."""
    if len(arr) <= 1:
        return arr  # Base case: A single-element or empty array is already sorted

    pivot = arr[0]  # Select the pivot element (first element in the array)
    # Partitioning the array into two subarrays
    less = [x for x in arr[1:] if x <= pivot]  # Elements less than or equal to the pivot
    greater = [x for x in arr[1:] if x > pivot]  # Elements greater than the pivot

    # Recursive calls to sort the subarrays and combining them with the pivot
    return quick_sort(less) + [pivot] + quick_sort(greater)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            