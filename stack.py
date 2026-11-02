class Stack:
    def __init__(self):
        self.items = []

    # Add an item to stack
    def push(self, item):
        self.items.append(item)

    # Remove the last added item
    def pop(self):
        if self.is_empty():
            return None

        return self.items.pop()

    # View the last added item
    def peek(self):
        if self.is_empty():
            return None

        return self.items[-1]

    # Check whether stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Display stack
    def display(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Stack items:", self.items)
