def heapify(arr, n, i):
    largest=i
    left=2*i+1
    right=2*i+2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        print(f"\nSwapping {arr[i]} and {arr[largest]}")
        arr[i], arr[largest] = arr[largest], arr[i]
        print("Heap after swap:", arr)
        heapify(arr, n, largest)
def heap_sort(arr):
    n = len(arr)
    print("Original Array:", arr)
    print("\nBuilding Max Heap:")
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        print(f"After heapify({i}):", arr)
        print("\nMax Heap Formed:", arr)
    print("\nSorting Process:")
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        print(f"\nMoved largest element to position {i}:")
        print(arr)
        heapify(arr, i, 0)
        print("Heap after heapify:", arr)
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("\nFinal Sorted Array:", arr)
