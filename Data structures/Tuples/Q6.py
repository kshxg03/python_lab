employee_salary = (20000, 25000, 30000)
name = ("Rabindra", "Bob", "Charlie")

employee_salary_list = list(employee_salary)
employee_salary_list[1] = 35000

employee_salary = tuple(employee_salary_list)

print(employee_salary)