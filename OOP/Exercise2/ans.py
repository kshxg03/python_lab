class Employee:
    def __init__(self, name, dob, age, salary, skillset):
        self.name = name
        self.dob = dob 
        self.age = age
        self.salary = salary
        self.skillset = skillset


class Developer(Employee):
    def __init__(self, name, dob, age, salary, skillset, github_link, is_fullstack):
        super().__init__(name, dob, age, salary, skillset)
        self.github_link = github_link
        self.is_fullstack = is_fullstack

    def display_profile(self): 
        return f"{self.name} has got skills: {self.skillset} with github link: {self.github_link}."


class HR(Employee):
    def __init__(self, name, dob, age, salary, skillset, is_manager, onboard_rate):
        super().__init__(name, dob, age, salary, skillset)
        self.is_manager = is_manager
        self.onboard_rate = onboard_rate

    @property
    def display_profile(self): 
        return f"{self.name} has got skills: {self.skillset} with onboard rate: {self.onboard_rate}."

d1 = Developer("Kshitiz", 2003, 22, 1000000, ["Python", "Git", "AI"], "http:kshxg03", True)
d2 = Developer("Aman", 2002, 23, 900000, ["JavaScript", "React"], "http:amanhub", True)
d3 = Developer("Ravi", 2001, 24, 850000, ["Python", "Git"], "http:ravihub", False)
d4 = Developer("Sita", 2000, 25, 950000, ["Java", "Spring"], "http:sitahub", True)
d5 = Developer("John", 1999, 26, 1100000, ["Python", "Git", "Django"], "http:johnhub", True)

developers_list = [d1, d2, d3, d4, d5]


h1 = HR("Ram", 1998, 27, 500000, ["Excel", "Communication"], True, "80%")
h2 = HR("Hari", 1997, 28, 550000, ["Management", "English"], False, "75%")

hr_list = [h1, h2]

print("Developers with Python and Git:\n")

for dev in developers_list:
    if "Python" in dev.skillset and "Git" in dev.skillset:
        print(dev.name)