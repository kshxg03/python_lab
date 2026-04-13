

# Store my_num as [1, 5, 7, 9]. Used reduce function to calculate product of these.

from functools import reduce


my_num = [1, 5, 7, 9]

product = reduce(lambda x, y: x * y, my_num)

print(product)
 