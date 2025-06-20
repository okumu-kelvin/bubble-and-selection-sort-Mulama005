def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the current element
        min_index = i
        # Find the minimum in the rest of the array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Test code (only for local testing — do NOT push to GitHub)
if __name__ == "__main__":
    test_array = [5, 4, 3, 2, 1, 0]
    sorted_array = selection_sort(test_array)
    print("Sorted:", sorted_array)

