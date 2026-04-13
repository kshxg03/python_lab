

num_list = [1, -3, 0, 2, 0, 7, 10, 8, -1]


def get_data(l, r, x):
    new_list = list(map(lambda n: x if n == 0 else n, num_list[l:r+1]))
    # print(new_list)
    return sum(new_list)


print(get_data(2, 7, 5))