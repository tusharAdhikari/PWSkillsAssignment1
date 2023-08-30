# Question Number 1 to 25

# 1. Reverse a string.
def reverse_string(s):
    return s[::-1]

# 2. Check if a string is a palindrome.
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# 3. Convert a string to uppercase.
def to_uppercase(s):
    return s.upper()

# 4. Convert a string to lowercase.
def to_lowercase(s):
    return s.lower()

# 5. Count the number of vowels in a string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for c in s if c in vowels)

# 6. Count the number of consonants in a string.
def count_consonants(s):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for c in s if c in consonants)

# 7. Remove all whitespaces from a string.
def remove_whitespaces(s):
    return ''.join(s.split())

# 8. Find the length of a string without using the len() function.
def custom_len(s):
    count = 0
    for _ in s:
        count += 1
    return count

# 9. Check if a string contains a specific word.
def contains_word(s, word):
    return word in s

# 10. Replace a word in a string with another word.
def replace_word(s, old_word, new_word):
    return s.replace(old_word, new_word)

# 11. Count the occurrences of a word in a string.
    return s.count(word)

# 12. Find the first occurrence of a word in a string.
def find_first_occurrence(s, word):
    return s.find(word)

# 13. Find the last occurrence of a word in a string.
def find_last_occurrence(s, word):
    return s.rfind(word)

# 14. Split a string into a list of words.
def split_string(s):
    return s.split()

# 15. Join a list of words into a string.
def join_words(lst):
    return ' '.join(lst)

# 16. Convert a string where words are separated by spaces to one where words are separated by underscores.
def space_to_underscore(s):
    return '_'.join(s.split())

# 17. Check if a string starts with a specific word or phrase.
def starts_with(s, prefix):
    return s.startswith(prefix)

# 18. Check if a string ends with a specific word or phrase.
def ends_with(s, suffix):
    return s.endswith(suffix)

# 19. Convert a string to title case (e.g., "hello world" to "Hello World").
def to_title_case(s):
    return s.title()

# 20. Find the longest word in a string.
def longest_word(s):
    words = s.split()
    return max(words, key=len)

# 21. Find the shortest word in a string.
def shortest_word(s):
    words = s.split()
    return min(words, key=len)

# 22. Reverse the order of words in a string.
def reverse_words(s):
    return ' '.join(reversed(s.split()))

# 23. Check if a string is alphanumeric.
def is_alphanumeric(s):
    return s.isalnum()

# 24. Extract all digits from a string.
def extract_digits(s):
    return ''.join(filter(str.isdigit, s))

# 25. Extract all alphabets from a string.
def extract_alphabets(s):
    return ''.join(filter(str.isalpha, s))