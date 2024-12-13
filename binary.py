def binary_search(arr, key):
    """Performs Binary Search on a sorted array to find the key."""
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Calculate the mid-point
        if arr[mid] == key:
            return mid  # Return index if key is found
        elif arr[mid] < key:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Key not found
