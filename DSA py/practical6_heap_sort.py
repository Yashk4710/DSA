
def heapify(arr, n, i):
    """
    Maintain the max-heap property for the subtree
    rooted at index i.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If root is not the largest, swap and heapify again
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Step 1: Build a Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current largest element to the end
        arr[0], arr[i] = arr[i], arr[0]

        # Restore max-heap property
        heapify(arr, i, 0)


# Main program
arr = list(map(int, input("Enter integers separated by spaces: ").split()))

print("Original Array:", arr)

heap_sort(arr)

print("Sorted Array:", arr)
