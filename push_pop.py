# Stack implementation using a list
class Stack:
    def __init__(self):
        self.items = []  # Initialize an empty list to hold stack elements

    def is_empty(self):
        return len(self.items) == 0  # Check if stack is empty

    def push(self, item):
        self.items.append(item)  # Add item to the top
        print(f"Pushed {item} to the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        item = self.items.pop()  # Remove and return top item
        print(f"Popped {item} from the stack.")
        return item

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            # Top is at the end of the list, so reverse to show top-first
            print("Stack contents (top to bottom):", self.items[::-1])


# Menu-driven program to interact with the stack
def main():
    stack = Stack()
    while True:
        print("\nStack Operations Menu:")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter the item to push: ")
            stack.push(item)  # Fixed: was 'stac k.push'
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.display()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()