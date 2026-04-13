marks_list = [83, 80, 92, 80, 67] #, [83, 88, 92, 89, 79], [80, 95, 77, 69, 66], [89, 92, 92, 98, 97], [78, 81, 76, 75, 65]

subjects_list = ["English", "Mathematics", "Science", "Economics", "Computer"]

min_marks = min(marks_list)
min_marks_id = marks_list.index(min_marks)

print("The subject with lowest marks is " + subjects_list[min_marks_id])