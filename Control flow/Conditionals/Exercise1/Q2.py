
# Ask user for num_1 and num_2. Display if num_1 is divisible by num_2 in format: 15 is [not] divisible by 3

num1 = int(input("Give a dividend: "))
num2 = int(input("Give a divisor: "))


if num1 % num2 == 0:
    print(f"{num1} is divisible by {num2}")
else:
    print(f"{num1} is not divisible by {num2}")

    