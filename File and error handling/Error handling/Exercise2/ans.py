
import csv
import json
from datetime import datetime

def can_drink(age):
    if type(age) == int:
        if age < 0:
            raise ValueError("Age must be greater than 0.")
        elif age > 100:
            raise AssertionError("Age must be greater than 100")
        elif age > 18:
            return True
        else:
            return False
    else:
        raise TypeError("Age must be an integer.")

def get_age(birth_year):
    current_year = datetime.now().year
    
    if not isinstance(birth_year, int):
        raise ValueError("Birth year must be an integer.")
    
    if birth_year < 1000:
        raise ValueError("Invalid birth year format.")
    
    if birth_year < 0 or birth_year > current_year:
        raise ValueError("Invalid birth year.")
    
    return current_year - birth_year


hard_drink = 0
soft_drink = 0

with open(r"C:\Users\Kshitiz\OneDrive\Documents\Downloads/employee_info.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        birth_year = int(row["DOB"])
        age = get_age(birth_year)
            
        if age >= 18:
            hard_drink += 1
        else:
            soft_drink += 1  
            
drink_data = {
    "hard_drink": hard_drink,
    "soft_drink": soft_drink
}

with open("drink_logistic.json", "w") as json_file:
    json.dump(drink_data, json_file, indent=4)

print("Drink logistics saved to drink_logistic.json")
