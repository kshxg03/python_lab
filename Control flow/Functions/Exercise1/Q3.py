
# Write a function is_palindrome(string) to check if a given string is palindrome or not. Return True if it is palindrome else return False.

def is_palindrome(string):
    reversed = string[::-1]
    if string.lower() == reversed.lower():
        return True
    else:
        return False

print(is_palindrome('madam'))