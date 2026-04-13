# Display numbers from 1 to 10 using both for and while loops.
num = 1

while num < 11:
    print(num, end=" ")
    num += 1

print(" ")

for i in range(1, 11):
    print(i, end=" ")

print(" ")

# Assign num_tuple as (1, 4, 7, 12, 20). Using loop, find even numbers and their sum
sum = 0
num_tuple = (1, 4, 7, 12, 20)
for num in num_tuple:
    if num % 2 == 0:
        sum = sum + num
print(sum)


# Assign num_set as {1, 3, 5, 7, 9}. Using loop, find odd numbers and their product
num_set = {1, 3, 5, 7, 9}
product = 1
for num in num_set:
    if num % 2 != 0:
        product = product * num
print(product)

# Assign num as 7. Display it's factorial using both for and while loops.
num = 7
factorial = num
while num > 1:
    factorial = factorial * (num-1)
    num = num-1
print(factorial)

num = 7
num_list = list(range(1, num+1))
fact = 1
for n in num_list:
    fact = fact * n
print(fact)

# Assign list with numbers. Find the second largest number in it using for loop.
my_list = [1, 2, 3, 4, 5, 6]

max_value = max(my_list)
second_max = 0
for num in my_list:
    if num > second_max and num < max_value:
        second_max = num
print(second_max)


# Assign set as {1, 4, 5, 7, 8, 12}. Generate new list evaluated_data using for loop such that odd number is doubled and even number is tripled. 
# If you encounter 4, skip evaluation for this and it you see 8, stop the loop.

set1 = {1, 4, 5, 7, 8, 12}
list1 = []

for num in set1:
    if num == 4:
        continue
    elif num == 8:
        break
    elif num % 2 == 0:
        num = num * 3
        list1.append(num)
    else:
        num = num * 2
        list1.append(num)

print(list1)
