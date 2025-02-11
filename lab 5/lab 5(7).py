stack = []

while True:
    print("\n Stack Menu")
    print("1. Push")
    print("2. Pop")

    
    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter the item to push: ")
        stack.append(item)
        print(f"{item} pushed into the stack.")
    
    elif choice == '2':
        if stack:
            print(f"Popped item: {stack.pop()}")
        else:
            print("Stack is empty! Cannot pop.")