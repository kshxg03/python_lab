
# Write a function get_product_remainder(num_1, num_2) that returns product and remainder of two numbers

def get_product_remainder(num_1, num_2):
    product = num_1 * num_2
    remainder = num_1 % num_2
    return product, remainder

product, remainder = get_product_remainder(3, 3)
print(f"Product: {product} and remainder: {remainder}")
