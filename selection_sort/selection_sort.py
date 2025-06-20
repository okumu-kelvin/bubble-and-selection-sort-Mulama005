def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == "__main__":
    test_array = [5, 4, 3, 2, 1, 0]
    sorted_array = selection_sort(test_array)
    print("Sorted:", sorted_array)

