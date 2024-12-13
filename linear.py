def linear_search(arr, key):
    """Performs a Linear Search on the array to find the key."""
    for index, element in enumerate(arr):
        if element == key:
            return index  # Return the index if the key is found
    return -1  # Return -1 if the key is not found
