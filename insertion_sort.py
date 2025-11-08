def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]  
        j = i - 1    
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
print("Insertion sort example")
arr_input = input("Enter the array elements separated by space: ")
arr = list(map(int, arr_input.split()))
print("Original array:", arr)
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)