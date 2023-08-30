# Question Number 26 to 50

# Question 26. Count the number of uppercase letters in a string.
def count_uppercase_letters(s):
    return sum(1 for c in s if c.isupper())

# Question 27. Count the number of lowercase letters in a string.
def count_lowercase_letters(s):
    return sum(1 for c in s if c.islower())

# Question 28. Swap the case of each character in a string.
def swap_case(s):
    return s.swapcase()

# Question 29. Remove a specific word from a string.
def remove_word(s, word):
    return s.replace(word, '')

# Question 30. Check if a string is a valid email address.
import re
def is_valid_email(s):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, s) is not None

# Question 31. Extract the username from an email address string.
def extract_username(email):
    return email.split('@')[0]

# Question 32. Extract the domain name from an email address string.
def extract_domain(email):
    return email.split('@')[1]

# Question 33. Replace multiple spaces in a string with a single space.
def replace_multiple_spaces(s):
    return ' '.join(s.split())

# Question 34. Check if a string is a valid URL.
import re
def is_valid_url(s):
    pattern = r'^(http|https)://[\w\.-]+\.\w+$'
    return re.match(pattern, s) is not None

# Question 35. Extract the protocol (http or https) from a URL string.
def extract_protocol(url):
    return url.split('://')[0]

# Question 36. Find the frequency of each character in a string.
def character_frequency(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return freq

# Question 37. Remove all punctuation from a string.
import string
def remove_punctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))

# Question 38. Check if a string contains only digits.
def contains_only_digits(s):
    return s.isdigit()

# Question 39. Check if a string contains only alphabets.
def contains_only_alphabets(s):
    return s.isalpha()

# Question 40. Convert a string to a list of characters.
def string_to_list(s):
    return list(s)

# Question 41. Check if two strings are anagrams.
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# Question 42. Encode a string using a Caesar cipher.
def caesar_cipher_encode(s, shift):
    encoded = []
    for char in s:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encoded_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encoded.append(encoded_char)
        else:
            encoded.append(char)
    return ''.join(encoded)

# Question 43. Decode a Caesar cipher encoded string.
def caesar_cipher_decode(encoded, shift):
    return caesar_cipher_encode(encoded, -shift)

# Question 44. Find the most frequent word in a string.
import re
from collections import Counter

def most_frequent_word(s):
    words = re.findall(r'\w+', s.lower())
    word_count = Counter(words)
    return word_count.most_common(1)[0][0]

# Question 45. Find all unique words in a string.
import re
def unique_words(s):
    return set(re.findall(r'\w+', s.lower()))

# Question 46. Count the number of syllables in a string.
def count_syllables(word):
    vowels = "AEIOUaeiou"
    count = 0
    for i in range(len(word)):
        if word[i] in vowels:
            if i == 0 or word[i - 1] not in vowels:
                count += 1
    return count

# Question 47. Check if a string contains any special characters.
def contains_special_characters(s):
    return any(not c.isalnum() and c != ' ' for c in s)

# Question 48. Remove the nth word from a string.
def remove_nth_word(s, n):
    words = s.split()
    if 1 <= n <= len(words):
        del words[n - 1]
        return ' '.join(words)
    return s

# Question 49. Insert a word at the nth position in a string.
def insert_at_nth_position(s, word, n):
    words = s.split()
    if 0 <= n <= len(words):
        words.insert(n, word)
        return ' '.join(words)
    return s

# Question 50. Convert a CSV string to a list of lists.
import csv
def csv_to_list_of_lists(s):
    reader = csv.reader([s])
    return list(reader)[0]