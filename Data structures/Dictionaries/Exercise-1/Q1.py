
# Assign student_info as {'name': 'Ram', 'age': 22, 'grade': 'A', 'courses': ['DS', 'SQL']}
# Find and display student's name, age, grade and courses enrolled with proper formatting
# Update student's grade to 'A+' and display updated dictionary
# Add 'level' key with value 'Beginner' and display updated dictionary
# Add one more course 'Python' to student's courses and display updated dictionary
# Remove age from student information and display updated dictionary
# Check if 'address' key is present in student information
# Find and display total number of items in student information
# Create a copy of this dictionary, update name to 'Bob', grade to 'B' and display both dictionary

student_info = {
    'name': 'Ram',
    'age': 22,
    'grade': 'A',
    'course': ['DS', 'SQL']
}

stdnt_name = student_info['name']
stdnt_age = student_info['age']
stdnt_grade = student_info['grade']
enrolled_courses = ", ".join(student_info['course'])

print(f"Students name is {stdnt_name}, age is {stdnt_age}, grade is {stdnt_grade} and courses enrolled are {enrolled_courses}")

student_info["grade"] = 'A+'
print(student_info)

student_info['level'] = 'Beginner'
print(student_info)

student_info['course'].append('Python')
print(student_info)

student_info.pop('age')
print(student_info)

print('address' in student_info)

print(len(student_info))

dict2 = student_info.copy()
dict2['name'] = 'Bob'
dict2['grade'] = 'B'
print(dict2)
