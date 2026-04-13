

# Store my_num as [1, 4, 7, 9, 12, 18]. Used filter function to select multiple of 3.

my_num = [1, 4, 7, 9, 12, 18]

divisible_checker = lambda x : x % 3 == 0
multiple_of_3 = list(filter(divisible_checker, my_num))
print(multiple_of_3)