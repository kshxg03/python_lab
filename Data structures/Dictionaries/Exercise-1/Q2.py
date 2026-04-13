
# Courses offered by college is stored in dictionary as 'course': ['DS', 'SQL', 'Python'], 'duration': [40, 50, 60]. Check if Python is offered in college
# College_1 has course as {'python': {'duration': 3, 'type': 'basic'}, 'java': {'duration': 4, 'type': 'medium'}}. College_2 has course as {'multimedia': {'duration': 2, 'type': 'basic'}, 'javascript': {'duration': 5, 'type': 'advanced'}}. College_1 acquired College_2. Update College_1 course with College_2's and display the updated result
# Assign translation_dict as {'hello': 'hola', 'thank you': 'gracias', 'goodbye': 'adios', ...}. Ask user to input a word in English and display its translation in Spanish. If word is not found, display Translation not found
# Using range function, generate a list of even numbers from 0 to 20 and display the result
# Using range, generate and display multiplicate of 3 from 30 to 1 in descending order

courses = {
    'course': ['DS', 'SQL','Python'],
    'duration': [40, 50, 60]
}

print('Python' in courses['course'])

College_1 = {'python': {'duration': 3, 'type': 'basic'}, 'java': {'duration': 4, 'type': 'medium'}}
College_2 = {'multimedia': {'duration': 2, 'type': 'basic'}, 'javascript': {'duration': 5, 'type': 'advanced'}}

College_1.update(College_2)
print(College_1)

translation_dict = {
    'hello': 'hola',
    'thank you': 'gracias',
    'goodbye': 'adios'
}

word = input("Enter a word in English: ").lower()

print("Spanish translation:", translation_dict.get(word, "Translation not found"))

nums_1 = list(range(0, 21, 2))
print(nums_1)

multiples_of_3 = list(range(30, 0, -3))
print(multiples_of_3)