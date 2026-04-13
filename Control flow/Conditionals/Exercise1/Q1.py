
# Ask user for name and birth year. Calculate and display if he/she can vote in format: Ram, You are [not] eligible for voting. (Note: 18+ people can vote)

name = input("What is your name? ").lower()
age = int(input("Whats ur age? "))

if age > 18:
    print(f"{name}, you are eligible to vote.")
else:
    print(f"{name}, you are not eligible to vote.")

    