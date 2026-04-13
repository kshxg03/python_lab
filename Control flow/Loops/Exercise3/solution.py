# Write function to take string as input and provide output with below condition:
# First letter of word always have to be capital
# If preceding letter occurs earlier in dictionary then letter has to be capital
# If preceding letter occurs later in dictionary then letter has to be small
# If preceding letter is same as current letter then no change in case.

def string_edit(user_input):
    new_list = []

    new_list.append(user_input[0])

    for iterator in range(1, len(user_input)):
        if  user_input[iterator - 1] == ' ':
            new_list.append(user_input[iterator].upper())
        elif  user_input[iterator - 1].lower() < user_input[iterator].lower():
            new_list.append(user_input[iterator].upper())
        elif user_input[iterator - 1].lower() > user_input[iterator].lower():
            new_list.append(user_input[iterator].lower())
        else:
            new_list.append(user_input[iterator])

    new_string = "".join(new_list)
    return new_string


# def string_edit(s):
#     word_list = s.split()
#     new_list = []
#     alphabets = 'abcdefghijklmnopqrstuvwxyz'

#     for each_word in word_list:
#         edited_word = ""  

#         for i in range(len(each_word)):
#             current = each_word[i].lower()

#             if i == 0:
#                 edited_word += current.upper()   
#             else:
#                 preceding = each_word[i - 1].lower()

#                 if alphabets.index(preceding) > alphabets.index(current):
#                     edited_word += current.upper()
#                 elif alphabets.index(preceding) < alphabets.index(current):
#                     edited_word += current.lower()
#                 else:
#                     edited_word += each_word[i] 

#         new_list.append(edited_word)

#     return " ".join(new_list)


print(string_edit("apple"))

            

# strr = 'abcdefghijklmnopqrstuvwxyz'

# print(strr[1])
        
