
# Store my_num as [1, 4, 7]. Used map function to calculate cube of each number.

my_num = [1, 4, 7]

num_cube = lambda x : x ** 3
cubed = list(map(num_cube, my_num))
print(cubed) 