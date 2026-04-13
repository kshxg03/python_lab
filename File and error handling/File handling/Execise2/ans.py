
# Create a csv file std_1.csv with columns: Name, Age, Grade. Add 5 records to it using list of list.


# import csv
# data = [["Name", "Age"], ["Rabindra", 30], ["Hari", 25]]
# with open("output.csv", "w", newline="") as file_obj:
# 	csv_writer = csv.writer(file_obj)
# 	csv_writer.writerows(data)
	
import csv
data = [["Name", "Age", "Grade"], ["Kshitiz", "22", "A+"], ["Aditya", "22", "A"], ["Yosh", "21", "A+"], ["Rishav", "21", "A+"], ["Rex", "21", "B"]]

with open("std_1.csv", "w") as file_obj:
    csv_writer = csv.writer(file_obj)
    csv_writer.writerows(data)

data = [{"Name": "Kshitiz", "Age": "22", "Grade": "A+"}, {"Name": "Aditya", "Age": "22", "Grade": "A"}, {"Name": "Yosh", "Age": "21", "Grade": "A+"}, {"Name": "Rishav", "Age": "21", "Grade": "A+"}, {"Name": "Rex", "Age": "21", "Grade": "B"}]

with open("std_2.csv", "w") as file_obj:
    fieldnames = ["Name", "Age", "Grade"]
    csv_writer = csv.DictWriter(file_obj, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(data)

with open(r"C:\Users\Kshitiz\OneDrive\Documents\Downloads/2022-01-03.csv", "r") as file_obj:
    csv_reader = csv.reader(file_obj)
    data1 = list(csv_reader)

print(data1)
print()


with open(r"C:\Users\Kshitiz\OneDrive\Documents\Downloads/2022-01-03.csv", "r") as file_obj:
    csv_reader = csv.DictReader(file_obj)
    data2 = list(csv_reader)

print(data2)