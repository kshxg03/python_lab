
# Ask user for string and check if it's palindrome in format: "madam" is [not] a palindrome

word = input("Whats the word? ")

reversed_word = word[::-1]

if word == reversed_word:
    print("The given word is a palindrome.")
else:
    print("The given word is not a palindrome.")