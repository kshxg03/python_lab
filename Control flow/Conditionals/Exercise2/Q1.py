
# Ask user for marks and display grade in format: Your grade is A. (Rule: 90+ => A, 80-90 => B, 70-80 => C, 60-70 => D, below 60 F)

marks = int(input("Whats your marks? "))

if marks > 90:
    print("Your grade is A.")
elif marks > 80 and marks < 90:
    print("Your grade is B.")
elif marks > 70 and marks < 80:
    print("Your grade is C.")
elif marks > 60 and marks < 70:
    print("Your grade is D.")
elif marks < 60:
    print("Your grade is E.")
else:
    print("Wrong input.")

