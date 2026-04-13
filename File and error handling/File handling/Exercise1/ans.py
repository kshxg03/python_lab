

text_for_file = "I love python"
file_content_for_java = ""

with open("Python.txt", "w") as file_obj:
    file_obj.write(text_for_file)


with open("Python.txt", "a") as file_obj:
    file_obj.write(" I will learn error handling")


with open("Python.txt", "r") as file_obj:
    file_content_for_java = file_obj.read().replace("Python", "Java").replace("python", "java")

# def word_changer(text):
#     word_list = text.split()
#     new_list = []
#     print(word_list)
#     for each in word_list:
#         if each.lower() == "python":
#             each = "java"
#             new_list.append(each)
#         elif each.lower() != "python":
#             each = each
#             new_list.append(each)

#     result = " ".join(new_list)
#     return result

with open("Java.txt", "w") as file_obj:
    file_obj.write(file_content_for_java)

import os

def get_file_size_in_kb(file_name):
    size_in_bytes = os.path.getsize(file_name)
    size_in_kb = size_in_bytes / 1024
    return size_in_kb

python_size = get_file_size_in_kb("python.txt")
java_size = get_file_size_in_kb("java.txt")

print(f"Size of python.txt: {python_size:.2f} KB")
print(f"Size of java.txt: {java_size:.2f} KB")


with open(r"C:\Users\Kshitiz\OneDrive\Documents\Downloads\nobel_prize_speech.txt", "r", encoding="utf-8") as file_obj:
    file_content = file_obj.read()

word_list = file_content.split()
# print(word_list)

count_dict = {}
# how to remove punctuations

def word_counter(words):
    for word in words:
        word = word.strip(".").strip(",") # Check translate function once
        count_dict[word] = word_list.count(word)

def return_max_repeated_word(word_dict):
    max_word = max(word_dict, key=word_dict.get)
    return max_word, word_dict[max_word]

word_counter(word_list)
print(return_max_repeated_word(count_dict))

