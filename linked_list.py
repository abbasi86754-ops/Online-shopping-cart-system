class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add product to cart
    def append(self, product, quantity):
        new_node = Node({
            "product": product,
            "quantity": quantity
        })

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    # Display all cart items
    def display(self):
        if self.head is None:
            print("\nYour cart is empty!")
            return

        current = self.head
        total = 0

        print("\n========== YOUR SHOPPING CART ==========")

        while current is not None:
            item = current.data
            product = item["product"]
            quantity = item["quantity"]

            subtotal = product["price"] * quantity
            total += subtotal

            print("Product:", product["name"])
            print("Quantity:", quantity)
            print("Price: Rs.", product["price"])
            print("Subtotal: Rs.", subtotal)
            print("----------------------------------------")

            current = current.next

        print("Total Bill: Rs.", total)
        print("========================================")

    # Search for a product in cart
    def find(self, product_id):
        current = self.head

        while current is not None:
            product = current.data["product"]

            if product["id"] == product_id:
                return current

            current = current.next

        return None

    # Update product quantity
    def update_quantity(self, product_id, new_quantity):
        node = self.find(product_id)

        if node is None:
            return False

        node.data["quantity"] = new_quantity
        return True

    # Remove product from cart
    def remove(self, product_id):
        if self.head is None:
            return False

        if self.head.data["product"]["id"] == product_id:
            self.head = self.head.next
            return True

        current = self.head

        while current.next is not None:
            if current.next.data["product"]["id"] == product_id:
                current.next = current.next.next
                return True

            current = current.next

        return False

    # Calculate total bill
    def calculate_total(self):
        total = 0
        current = self.head

        while current is not None:
            item = current.data
            product = item["product"]

            total += product["price"] * item["quantity"]
            current = current.next

        return total

    # Check whether cart is empty
    def is_empty(self):
        return self.head is None
