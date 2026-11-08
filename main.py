from linked_list import LinkedList
from stack import Stack
from queue import OrderQueue
from algorithms import linear_search, bubble_sort
from products import products


# Main Shopping System
def main():

    cart = LinkedList()
    undo_stack = Stack()
    order_queue = OrderQueue()

    while True:

        print("\n======================================")
        print("       ONLINE SHOPPING CART SYSTEM")
        print("======================================")
        print("1. View Products")
        print("2. Add Product to Cart")
        print("3. View Shopping Cart")
        print("4. Update Cart Quantity")
        print("5. Remove Product from Cart")
        print("6. Search Product")
        print("7. Sort Products by Price")
        print("8. Undo Last Add")
        print("9. Checkout / Place Order")
        print("0. Exit")
        print("======================================")

        choice = input("Enter your choice: ")

        # 1. View Products
        if choice == "1":

            print("\nAVAILABLE PRODUCTS")

            for product in products:
                print(
                    "ID:", product["id"],
                    "| Name:", product["name"],
                    "| Category:", product["category"],
                    "| Price: Rs.", product["price"],
                    "| Stock:", product["stock"]
                )

        # 2. Add Product
        elif choice == "2":

            try:
                product_id = int(input("Enter Product ID: "))
                quantity = int(input("Enter Quantity: "))
            except ValueError:
                print("Please enter valid numbers!")
                continue

            product = linear_search(products, product_id)

            if product is None:
                print("Product not found!")

            elif quantity <= 0:
                print("Quantity must be greater than zero!")

            elif quantity > product["stock"]:
                print("Not enough stock available!")

            elif cart.find(product_id) is not None:
                print("Product is already in cart. Use Update Quantity.")

            else:
                cart.append(product, quantity)
                undo_stack.push(product_id)

                print("Product successfully added to cart!")

        # 3. View Cart
        elif choice == "3":

            cart.display()

        # 4. Update Quantity
        elif choice == "4":

            try:
                product_id = int(input("Enter Product ID: "))
                new_quantity = int(input("Enter New Quantity: "))
            except ValueError:
                print("Please enter valid numbers!")
                continue

            node = cart.find(product_id)

            if node is None:
                print("Product not found in cart!")

            elif new_quantity <= 0:
                print("Quantity must be greater than zero!")

            elif new_quantity > node.data["product"]["stock"]:
                print("Requested quantity exceeds available stock!")

            else:
                cart.update_quantity(product_id, new_quantity)
                print("Quantity updated successfully!")

        # 5. Remove Product
        elif choice == "5":

            try:
                product_id = int(input("Enter Product ID to remove: "))
            except ValueError:
                print("Please enter a valid Product ID!")
                continue

            if cart.remove(product_id):
                print("Product removed successfully!")
            else:
                print("Product not found in cart!")

        # 6. Search Product
        elif choice == "6":

            try:
                product_id = int(input("Enter Product ID to search: "))
            except ValueError:
                print("Please enter a valid Product ID!")
                continue

            result = linear_search(products, product_id)

            if result:
                print("\nProduct Found!")
                print("Name:", result["name"])
                print("Category:", result["category"])
                print("Price: Rs.", result["price"])
                print("Available Stock:", result["stock"])
            else:
                print("Product not found!")

        # 7. Sort Products
        elif choice == "7":

            sorted_products = bubble_sort(products)

            print("\nPRODUCTS SORTED BY PRICE")

            for product in sorted_products:
                print(
                    product["name"],
                    "- Rs.",
                    product["price"]
                )

        # 8. Undo Last Add
        elif choice == "8":

            last_product_id = undo_stack.pop()

            if last_product_id is None:
                print("Nothing to undo!")

            elif cart.remove(last_product_id):
                print("Last added product removed successfully!")

            else:
                print("The last added product is no longer in your cart.")

        # 9. Checkout
        elif choice == "9":

            if cart.is_empty():
                print("Your cart is empty!")
                continue

            # Check stock again before checkout
            current = cart.head
            stock_available = True

            while current is not None:
                item = current.data
                product = item["product"]

                if item["quantity"] > product["stock"]:
                    stock_available = False
                    print("Insufficient stock for:", product["name"])

                current = current.next

            if not stock_available:
                print("Please update your cart before checkout.")
                continue

            total = cart.calculate_total()

            # Create order details
            order_items = []
            current = cart.head

            while current is not None:
                item = current.data

                order_items.append({
                    "product": item["product"],
                    "quantity": item["quantity"]
                })

                current = current.next

            order = {
                "items": order_items,
                "total": total
            }

            # Add order to Queue
            order_queue.enqueue(order)

            print("\nOrder added to processing queue!")

            # Process first order
            processed_order = order_queue.dequeue()

            # Update product stock
            for item in processed_order["items"]:
                item["product"]["stock"] -= item["quantity"]

            print("\n========== FINAL INVOICE ==========")

            for item in processed_order["items"]:
                product = item["product"]
                quantity = item["quantity"]

                print("Product:", product["name"])
                print("Quantity:", quantity)
                print("Subtotal: Rs.", product["price"] * quantity)
                print("----------------------------------")

            print("Total Bill: Rs.", processed_order["total"])
            print("Order Status: Processed")
            print("==================================")

            # Empty cart and undo history
            cart = LinkedList()
            undo_stack = Stack()

        # 0. Exit
        elif choice == "0":

            print("\nThank you for shopping!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


# Start Program
if __name__ == "__main__":
    main()