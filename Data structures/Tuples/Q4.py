employee_salary = (20000, 25000, 30000)
name = ("Rabindra", "Bob", "Charlie")

lowest_salary = min(employee_salary)
indx_lowest_salary = employee_salary.index(lowest_salary)

print("Employee with highest salary: " + name[indx_lowest_salary])