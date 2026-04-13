

# Ask user for name, age and salary. 
# Display if user is eligible for a loan in format: Ram, You are [not] eligible for loan. (Eligibility Rule: Age between 21 and 60, salary at least 30K)

name = input("What is your name? ").lower()
age = int(input("Whats ur age? "))
salary = int(input("Whats ur salary? "))

if age > 21 and age < 60 and salary >= 30000:
    print(f"{name}, you are eligible for a loan.")
else:
    print(f"{name}, you are not eligible for a loan.")
