def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        # Flag to optimize the algorithm by checking if any swaps occurred
        swapped = False

        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Swap the elements if they are in the wrong order
                value = arr[j]
                #arr[j], arr[j + 1] = arr[j + 1], arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = value
                swapped = True

        # If no swaps occurred in this pass, the list is already sorted
        if not swapped:
            break

# Example usage:
if __name__ == "__main__":
    numbers = [10, 5, 15, 3, 20]
    
    print("Original list:", numbers)

    bubble_sort(numbers)

    print("Sorted list:", numbers)