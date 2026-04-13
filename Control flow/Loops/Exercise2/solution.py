
# Record of student is stored as {'9843': {'course': 'Python', 'name': 'Ram', 'present': False}, {'9844': {'course''Java', 'name': 'Shyam', 'present': True}}. 
# Using loop, display name of student who are absent in Python class.: 

std_record = {'9843': {'course': 'Python', 'name': 'Ram', 'present': False}, '9844': {'course': 'Java', 'name': 'Shyam', 'present': True}, '9845': {'course': 'Python', 'name': 'Hari', 'present': False}}

for std in std_record:
    if (std_record[std]['course']) == "Python" and (std_record[std]['present']) == False:
        print(std_record[std]['name'])
                                                                              

# Store a fruits names in a list. Generate a new list from it such that if fruit name starts with a/A then it has to be converted to uppercase else it has to be converted to lowercase.
# Use both for loop and list comprehension.

fruits_list = ['apple', 'banana', 'Pear', 'Mango']

new_list = [x.upper() if x.startswith("a") or x.startswith("A") else x.lower() for x in fruits_list]

print(new_list)


# Write function to check if a number is prime or not. Using this function, generate list of first 20 prime numbers.

def prime_checker(num):

    if num < 1 or num == 1:
        return False
    elif num == 2:
        return True
    elif num > 2:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

prime_list = []

for i in range(1, 21):
    if prime_checker(i) == "Not prime":
        continue
    elif prime_checker(i) == "Prime":
        prime_list.append(i)
print(prime_list)


# Write function that accepts string from user and returns a dictionary for occurrences of a character in it. Ex: apple => {'a': 1, 'p': 2, 'l': 1, 'e': 1}.

user_input = input("Type a word: ")

dict1 = {}

for each in user_input:
    occurence = user_input.count(each)
    dict1[each] = occurence

print(dict1)










