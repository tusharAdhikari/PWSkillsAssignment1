# Challenge Level:
# 31. generate a list of prime numbers using the Sieve of Eratosthenes algorithm and list comprehension.
def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    return [num for num, is_prime in enumerate(primes) if is_prime]
prime_list = sieve_of_eratosthenes(50)
print(prime_list)


# 32.  generates a list of all Pythagorean triplets up to a specified limit using list comprehension.
limit = 20
pythagorean_triplets = [(a, b, c) for a in range(1, limit) for b in range(a, limit) for c in range(b, limit) if a**2 + b**2 == c**2]


# 33. generates a list of all possible combinations of two lists using list comprehension.
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combinations = [(x, y) for x in list1 for y in list2]


# 34. calculates the mean, median, and mode of a list of numbers using list comprehension.
from statistics import mean, median, mode

your_list = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]
mean_value = mean(your_list)
median_value = median(your_list)
mode_value = mode(your_list)


# 35. generates Pascal's triangle up to a specified number of rows using list comprehension.
from math import factorial

def generate_pascals_triangle(rows):
    return [[factorial(i)//(factorial(j)*factorial(i-j)) for j in range(i+1)] for i in range(rows)]


# 36. calculates the sum of the digits of a factorial of numbers from 1 to 5 using list comprehension.
factorial_sums = [sum(int(digit) for digit in str(factorial(num))) for num in range(1, 6)]


# 37. finds the longest word in a sentence using list comprehension.
sentence = "This is a sample sentence."
longest_word = max((word.strip(".,") for word in sentence.split()), key=len)


# 38. filters a list of strings to include only those with more than three vowels using list comprehension.
vowel_count = lambda s: sum(1 for char in s if char.lower() in 'aeiou')
filtered_list = [string for string in your_list if vowel_count(string) > 3]


# 39. calculates the sum of the digits of numbers from 1 to 1000 using list comprehension.
sum_of_digits = [sum(int(digit) for digit in str(num)) for num in range(1, 1001)]


# 40. generates a list of prime palindromic numbers using list comprehension.
def is_palindrome(n):
    return str(n) == str(n)[::-1]

prime_palindromes = [num for num in sieve_of_eratosthenes(1000) if is_palindrome(num)]

