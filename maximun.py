# Program to find the maximum number in an array
def find_maximum(arr):
    if not arr:  # Check if array is empty
        return None
    max_num = arr[0]  # Initialize max_num as the first element
    for num in arr:  # Iterate through the array
        if num > max_num:
            max_num = num  # Update max_num if current number is larger
    return max_num

# Main function to take user input and find maximum
def main():
    # Input array size and elements
    try:
        size = int(input("Enter the size of the array: "))
        if size <= 0:
            print("Array size must be positive.")
            return
        
        arr = []
        print(f"Enter {size} numbers:")
        for i in range(size):
            num = float(input(f"Enter element {i+1}: "))  # Accept integers or floats
            arr.append(num)
        
        # Display the array
        print("Array:", arr)
        
        # Find and display the maximum
        max_num = find_maximum(arr)
        if max_num is None:
            print("Array is empty.")
        else:
            print("Maximum number in the array:", max_num)
    
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

# Run the program
if __name__ == "__main__":
    main()