def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print("Linear Search Example")
arr_input = input("Enter the array elements separated by space: ")
arr = list(map(int, arr_input.split()))
target = int(input("Enter the target element to search: "))
result = linear_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")
