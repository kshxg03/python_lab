

# Ask user for hour of the day (0-23) 
# and display appropriate greeting in format: Good Morning. (Rule: 5-12 => Good Morning, 12-17 => Good Afternoon, 17-21 => Good Evening, 21-5 => Good Night, else invalid time)

hour = int(input("Enter hour of the day (0-23): "))

if 5 <= hour < 12:
    print("Good Morning.")
elif 12 <= hour < 17:
    print("Good Afternoon.")
elif 17 <= hour < 21:
    print("Good Evening.")
elif (21 <= hour <= 23) or (0 <= hour < 5):
    print("Good Night.")
else:
    print("Invalid time")