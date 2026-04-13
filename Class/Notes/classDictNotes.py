# what can be used as key, list, tuple, int
# .get to get key value
# .keys, .values, .items
# range function

# my_dict = {
#     1: "one",
#     2: "two",
#     3: "three"
# }

# my_dict[3] = 4
# print(my_dict)

# course_info_1 = {"python": 1, "data_science": 2}
# course_info_2 = {"ml": 2, "django": 2, "python": 1.2}

# course_info_1.update(course_info_2)

# print(course_info_1)

# str  = "cat"
# print(str[0])


# num_1 = -5

# if num_1 > 0 and num_1%2 == 0:
#     print("Positive even")
# elif num_1 > 0 and num_1%2 != 0:
#     print("Negative odd")
# elif num_1 < 0:
#     print("Negative")
# elif num_1 == 0:
#     print("Zero")
# else:
#     print("Other")


# def circle_area(diameter):
#     radius = diameter/2
#     pie = 3.14
#     area = pie*radius*radius

#     if diameter < 0:
#         print("Invalid number")
#     else:
#         print(f"{area:.2f}")
        
# diameter = int(input("What is the diameter? "))

# circle_area(diameter)

# age_checker = lambda x : x > 16

# age_list = [1, 12, 13, 14, 15, 16, 17, 18, 22, 21 , 29, 20]

# age_greater_than_16 = list(filter(age_checker, age_list))

# print(age_greater_than_16)

# from functools import reduce

# def producter(num1, num2):
#     return num1 * num2

# data = [1, 3, 4] 
# result = reduce(producter, data)
# print(result)

# def age_categorizer(age):
#     if age >=0 and age <=1:
#         return "infant"
#     elif age >= 2 and age <=11:
#        return "child"  
#     elif age >= 12 and age <=20:
#        return "teenager"

# age_list = [1, 3, 4, 8, 12, 20]
# categorized_ages = list(map(age_categorizer, age_list))
# print(categorized_ages)

# alphabets = ['k', 'a', 'b', 'n']

# for items in alphabets:
#     print(items.upper())
#     print()

# new_list = []
# num_list = [1, 4, 4, 7, 9]

# for num in num_list:
#     divided_num = num/2
#     new_list.append(divided_num)

# print(new_list)

# num_list = range(1, 11)

# user_num = int(input("What is the number? "))

# for num in num_list:
#     result = num * user_num
#     print(f"{user_num} * {num:>2} = {result:>2}")

# for i in range(6):
#     for j in range(1, i+1):
#         print("* ", end="")
#     print(" ")


# OOP

# class Car:
#     def __init__(self, brand, model, color="blue"):
#         self.brand = brand
#         self.model = model
#         self.color = model

# car_1 = Car("Toyota", "Fortuner")

# print(car_1.color)

# crate a class named people
# it should have two attribute name and birth_year
# create two objects using this class
# dipslay their name and age using f-string

# class People:
#     def __init__(self, name, birth_year):
#         self.name = name
#         self.birth_year = birth_year

#     @property
#     def get_user_age(self):
#         return 2026 - self.birth_year

#     def __repr__(self):
#         return f"{self.name} is of {self.get_user_age}."
    
#     def is_adult(self):
#         user_age = self.get_user_age
#         if user_age > 18:
#             return True
#         else:
#             return False

# class Player(People):
#     def __init__(self, name, birth_year, club, country):
#         super().__init__(name, birth_year)
#         self.club = club
#         self.country = country

#     def shoot(self):
#         return f"{self.name} is shooting."
    

# p1 = Player("Ronaldo", 1977, "Real madrid", "Portugal")
# p2 = Player("Messi", 1979, "Barcelona", "Argentina")

# print(p1)
# print(p2)
# print(f"{p1.shoot()}")
# print(f"{p2.shoot()}")

# person1 = People("Rex", 2001)
# person2 = People("Kshitiz", 2003)
# print(person1)
# print(person2)

# print(person1.is_adult())
# year = 2026

# def display_details(obj):
#     name = obj.name
#     birth_year = obj.birth_year
#     age = year - birth_year
#     return name, age

# # birth_year1 = person1.birth_year
# # birth_year2 = person2.birth_year
# # age1 = year - birth_year1
# # age2 = year - birth_year2
# # name1 = person1.name
# # name2 = person2.name

# name1, age1 = display_details(person1)
# name2, age2 = display_details(person2)
# print(f"Name: {name1}, age: {age1}")
# print(f"Name: {name2}, age: {age2}")


# class Student(People):
#     def __init__(self, name, birth_year, course_enrolled, mobile_number, fee_paid, email):
#         super().__init__(name, birth_year)
#         self.course_enrolled = course_enrolled
#         self.mobile_number = mobile_number
#         self.fee_paid = fee_paid
#         self.email = email

# s1 = Student("Ram", 1999, "python", 98455, True, "aaa@gmail.com")
# print(s1.get_user_age)

# create a new class called a player inheriting people
# player should have attribute: name, birth_year, club, country
# player should have method: shoot() which should return player is shooting
# assign two player using class players
# print age of each player
# call method shoot on each of them 


# class Nepali:
# 	def __init__(self, name):
# 		self.name = name

# 	def greet(self):
# 		return f"Namaste, {self.name}!"

# class English:
# 	def __init__(self, name):
# 		self.name = name

# 	def greet(self):
# 		return f"Hello, {self.name}!"
	
# def talk(obj_name):
# 	return obj_name.greet()

# n1 = Nepali("Hari")
# print(talk(n1))

# class Animal:
#     def speak(self):
#         return "Animal speech"
    
# class Dog(Animal):
#     pass
#     # def speak(self):
#     #     return "woof"
    
# d1 = Dog()
# print(d1.speak())

# class Vector3D:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __repr__(self):
#         return f"({self.x}, {self.y}, {self.z})"
    
#     def __add__(self, other):
#         sum_x = self.x + other.x
#         sum_y = self.y + other.y
#         sum_z = self.z + other.z    
#         result_vector = Vector3D(sum_x, sum_y, sum_z)    
#         return result_vector

#     def __sub__(self, other):
#         diff_x = self.x - other.x
#         diff_y = self.x - other.y
#         diff_z = self.z - other.z
#         result_vector = Vector3D(diff_x, diff_y, diff_z)
#         return result_vector
        
#     def __lt__(self, other):
#         vec_1_mag = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
#         vec_2_mag = (other.x ** 2 + other.y ** 2 + other.z ** 2) ** 0.5
#         return vec_1_mag < vec_2_mag
    
# vec_1 = Vector3D(5, -1, 2)
# vec_2 = Vector3D(3, 1, 6)

# print(vec_1 - vec_2)

# import os

# files = os.listdir(r"E:\PythonCW")
# print(files)

# import random
# names = ["pratik", "bijay", "urgyen", "kshitiz"]
# random.randint(1, 6)
# random.choice(names)
# random.sample(names, 2)
# random.shuffle(names)
# print(names)
# random.seed(40)
# winner = random.choice(names)
# print(winner)

# import math

# number = 1.1678910
# print(math.floor(number))
# print(math.ceil(3.2))
# print(math.sqrt(49))
# print(math.pow(2, 5))
# print(math.pi)
# print(math.degrees(2 * math.pi))
# print(math.radians(360))
# print(math.sin(math.pi/2))
# print(math.log(100, 10))
# print(math.gcd(12, 18))
# print(math.lcm(12, 18))

# from datetime import datetime

# current_time = datetime.now()
# print(current_time)

# from datetime import date, timedelta

# today = date.today()
# days_before_week = today - timedelta(weeks=1)
# print(days_before_week)


# from mailerpy import Mailer

# password = "azjr ipni zrnk duru"

# my_mailer = Mailer("smtp.gmail.com", 587, "kshitizshrestha2003@gmail.com", password)

# to_email = ["kshitizshrestha2003@gmail.com"]
# subject = "Test from python"
# body = f""" 
# Hello guys,

# This is from code

# Regards,
# Automation Engine
# """

my_mailer.send_mail(to_email, subject, body)


