def counting_sort(arr, exp, base=10):
    n = len(arr)
    output = [0] * n 
    count = [0] * base 
    
    for i in range(n):
        digit = (arr[i] // exp) % base
        count[digit] += 1
    for i in range(1, base):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        digit = (arr[i] // exp) % base
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr:
        return arr
    max_num = max(arr)
    exp = 1  
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10 
    return arr

print("Radix sort example")
arr_input = input("Enter the array elements separated by space: ")
arr = list(map(int, arr_input.split()))
print("Original array:", arr)
sorted_arr = radix_sort(arr)
print("Sorted array:", sorted_arr)