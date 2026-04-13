
# Ask user for two numbers and display the largest in format: The largest number is 5

num1 = int(input("number 1: "))
num2 = int(input("number 2: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num2 > num1:
    print(f"{num2} is greater than {num1}.")
else:
    print("They're equal.")