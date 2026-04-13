

# Write a function greet() that takes name of student and course enrolled.
# It has to return Hello, {name}, Welcome to {course} class. Note: If course is not passed it has to be Python in default

def greet(name, course = "python"):
    return f"Hello {name}, welcome to {course} class."

print(greet('kshitiz'))
