import heapq

print("Task 1 program started.")

# Predefined Product Array
default_products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 45},
    {"name": "Monitor", "price": 300},
    {"name": "Smartphone", "price": 800},
]

# Merge Sort Implementation
def merge_sort(arr, key):
    if len(arr) <= 1:
         # Base case: A single-element array is already sorted
        return arr
    # Find the midpoint
    
    mid = len(arr) // 2
     # Sort the left half recursively
    left = merge_sort(arr[:mid], key)
    #  Sort the right half recursively
    right = merge_sort(arr[mid:], key)
    return merge(left, right, key)
#     """Merges two sorted arrays into a single sorted array."""
def merge(left, right, key):
    # Temporary array to hold sorted elements
    sorted_array = []
    while left and right:
        if left[0][key] <= right[0][key]:
            sorted_array.append(left.pop(0))
        else:
              # Append the smaller element
            sorted_array.append(right.pop(0))
            
            #  Append remaining elements from left or right
    return sorted_array + left + right

# Quick Sort Implementation
def quick_sort(arr, key):
    if len(arr) <= 1:
        # Base case: A single-element or empty array is already sorted
        return arr
    # Select the pivot element (first element in the array)
    pivot = arr[0]
     # Elements less than or equal to the pivot
    less = [x for x in arr[1:] if x[key] <= pivot[key]]
     # Elements greater than the pivot
    greater = [x for x in arr[1:] if x[key] > pivot[key]]
        
        # Recursive calls to sort the subarrays and combining them with the pivot
    return quick_sort(less, key) + [pivot] + quick_sort(greater, key)

# Heap Sort Implementation
def heapify(arr, n, i, key):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left][key] > arr[largest][key]:
        largest = left
    if right < n and arr[right][key] > arr[largest][key]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key)

def heap_sort(arr, key):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, key)
    return arr

# Distribution Sort Implementation
def distribution_sort(arr, key):
    if not arr:
        return []
    
    # Find the range of the key
    min_price = min(item[key] for item in arr)
    max_price = max(item[key] for item in arr)
    range_price = max_price - min_price + 1

    # Create buckets
    buckets = [[] for _ in range(range_price)]

    # Place elements into buckets
    for item in arr:
        index = int(item[key] - min_price)
        buckets[index].append(item)

    # Concatenate all buckets
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array

# Linear Search Implementation
def linear_search(arr, key, value):
    for i, product in enumerate(arr):
        if product[key] == value:
            # Return the index if the key is found
            return i
        # return -1 if the key is not found

    return -1

# Binary Search Implementation
def binary_search(arr, key, value):
    low, high = 0, len(arr) - 1
 
    while low <= high:
        # Calculate the mid-point
        mid = (low + high) // 2
        if arr[mid][key] == value:
            # Return index if key is found
            return mid
        elif arr[mid][key] < value:
             # Search in the right half
            low = mid + 1
        else:
            # Search in the left half
            high = mid - 1
            # Key not found
    return -1

# Main Function
def main():
    # Prompt user for array input or use predefined array
    print("Would you like to input your own array of products or use the default array?")
    choice = input("Enter '1' for custom array or '2' for default array: ")
    if choice == '1':
        products = []
        n = int(input("How many products would you like to enter? "))
        for _ in range(n):
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            products.append({"name": name, "price": price})
    else:
        products = default_products

    # Displaying the products before sorting
    print("\nOriginal Product List:")
    for product in products:
        print(product)

    # Allow the user to choose sorting algorithms
    print("\nChoose the first sorting algorithm:")
    print("1. Merge Sort")
    print("2. Quick Sort")
    print("3. Heap Sort")
    print("4. Distribution Sort")
    sort_choice1 = int(input("Enter the number of your choice: "))

    print("\nChoose the second sorting algorithm:")
    print("1. Merge Sort")
    print("2. Quick Sort")
    print("3. Heap Sort")
    print("4. Distribution Sort")
    sort_choice2 = int(input("Enter the number of your choice: "))

    # Sort products based on price
    sort_algorithms = {
        1: merge_sort,
        2: quick_sort,
        3: heap_sort,
        4: distribution_sort
    }

    sorted_products1 = sort_algorithms[sort_choice1](products, "price")
    sorted_products2 = sort_algorithms[sort_choice2](products, "price")

    # Displaying sorted products
    print("\nProducts sorted by price using algorithm 1:")
    for product in sorted_products1:
        print(product)

    print("\nProducts sorted by price using algorithm 2:")
    for product in sorted_products2:
        print(product)

    # Allow the user to choose a search algorithm
    print("\nChoose a search algorithm:")
    print("1. Linear Search")
    print("2. Binary Search")
    search_choice = int(input("Enter the number of your choice: "))

    # Perform search
    search_value = float(input("Enter the price of the product you want to search for: "))
    if search_choice == 1:
        result = linear_search(sorted_products1, "price", search_value)
    elif search_choice == 2:
        result = binary_search(sorted_products1, "price", search_value)

    if result != -1:
        print(f"Product found: {sorted_products1[result]}")
    else:
        print("Product not found.")

if __name__ == "__main__":
    main()



