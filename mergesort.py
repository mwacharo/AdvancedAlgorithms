# def merge_sort(arr):
#     """Recursively sorts an array using Merge Sort algorithm."""
#     if len(arr) <= 1:
#         return arr  # Base case: A single-element array is already sorted
    
#     mid = len(arr) // 2  # Find the midpoint
#     left = merge_sort(arr[:mid])  # Sort the left half recursively
#     right = merge_sort(arr[mid:])  # Sort the right half recursively
    
#     return merge(left, right)  # Merge sorted halves

# def merge(left, right):
#     """Merges two sorted arrays into a single sorted array."""
#     sorted_array = []  # Temporary array to hold sorted elements
#     while left and right:  # While both arrays have elements
#         if left[0] <= right[0]:  # Compare the smallest elements
#             sorted_array.append(left.pop(0))  # Append the smaller element
#         else:
#             sorted_array.append(right.pop(0))  # Append the smaller element
    
#     # Append remaining elements from left or right
#     return sorted_array + left + right


def merge_sort(arr, key):
    """
    Sorts an array of dictionaries by a given key using Merge Sort.
    
    Parameters:
        arr (list): The list to be sorted.
        key (str): The key in the dictionaries by which to sort (e.g., "price").
        
    Returns:
        list: The sorted array.
    """
    if len(arr) <= 1:
        return arr  # Base case: a list of one element is already sorted

    # Find the middle point and divide the list into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)  # Recursively sort the left half
    right = merge_sort(arr[mid:], key)  # Recursively sort the right half
    
    # Merge the two sorted halves
    return merge(left, right, key)

def merge(left, right, key):
    """
    Merges two sorted lists into a single sorted list based on the given key.
    
    Parameters:
        left (list): The left sorted list.
        right (list): The right sorted list.
        key (str): The key in the dictionaries by which to merge.
        
    Returns:
        list: The merged and sorted list.
    """
    sorted_array = []
    while left and right:
        if left[0][key] <= right[0][key]:  # Compare based on the key (e.g., "price")
            sorted_array.append(left.pop(0))
        else:
            sorted_array.append(right.pop(0))
    
    # Append any remaining elements from either list
    return sorted_array + left + right

# Example array of products
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 45},
    {"name": "Monitor", "price": 300},
    {"name": "Smartphone", "price": 800},
]

# Sort the products by price
sorted_products = merge_sort(products, key="price")

# Print the sorted products
print("Sorted products by price:")
for product in sorted_products:
    print(product)
