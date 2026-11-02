# Linear Search Algorithm
def linear_search(products, product_id):

    for product in products:

        if product["id"] == product_id:
            return product

    return None


# Bubble Sort Algorithm
def bubble_sort(products):

    sorted_products = products.copy()

    n = len(sorted_products)

    for i in range(n):

        for j in range(0, n - i - 1):

            if sorted_products[j]["price"] > sorted_products[j + 1]["price"]:

                sorted_products[j], sorted_products[j + 1] = (
                    sorted_products[j + 1],
                    sorted_products[j]
                )

    return sorted_products
