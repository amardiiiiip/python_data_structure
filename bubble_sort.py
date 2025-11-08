def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
       
        swapped = False
        
        
        for j in range(0, n-i-1):
           
            if arr[j] > arr[j+1]:
               
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
       
        if not swapped:
            break
    
    return arr

print("Bubble sort example")
arr_input = input("Enter the array elements separated by space: ")
arr = list(map(int, arr_input.split()))
print("Original array:", arr)
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)