
# Write a function count_vowels(string) return the number of vowels in a given string.

def count_vowels(string):
    string = string.lower()
    return (
        string.count('a') +
        string.count('e') +
        string.count('i') +
        string.count('o') +
        string.count('u')
    )

print(count_vowels('kshitiz'))
