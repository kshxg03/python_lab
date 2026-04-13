
# Ask user for birth year and display life stage in format: You are a teenager. (Rule: 0-12 => Child, 13-19 => Teenager, 20-59 => Adult, 60+ => Senior)

birth_year = int(input("Whats your birth year? "))

age = 2025 - birth_year

if age > 0 and age < 12:
    print("You are a child.")
elif age > 13 and age < 19:
    print("You are a teenager.")
elif age > 20 and age < 59:
    print("You are a adult.")
elif age > 60:
    print("You are a senior.")
else:
    print("Wrong input.")
    
    