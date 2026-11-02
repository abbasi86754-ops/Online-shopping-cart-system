class OrderQueue:
    def __init__(self):
        self.orders = []

    # Add a new order
    def enqueue(self, order):
        self.orders.append(order)

    # Process the first order
    def dequeue(self):
        if self.is_empty():
            return None

        return self.orders.pop(0)

    # View the first order
    def peek(self):
        if self.is_empty():
            return None

        return self.orders[0]

    # Check whether queue is empty
    def is_empty(self):
        return len(self.orders) == 0

    # Display all pending orders
    def display(self):
        if self.is_empty():
            print("No pending orders!")
        else:
            print("Pending Orders:", self.orders)
