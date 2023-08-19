#Question2: Take the string from user and counts the number of vowels (a, e, i, o, u) in the string.

sentence = input("Enter a sentence: ")
# Define a function to count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
    return vowel_count
num_vowels = count_vowels(sentence)
print("Number of vowels in the sentence:", num_vowels)
