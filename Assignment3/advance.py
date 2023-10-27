# Advanced Level:
your_list = []  #modify the list
# 21. calculates the sum of the digits of numbers in a list using a list comprehension.
digit_sum_list = [sum(int(digit) for digit in str(num)) for num in your_list]

# 22. find the prime factors of a given number using a `for` loop and list comprehension.
def prime_factors(n):
    return [i for i in range(2, n + 1) if n % i == 0 and all(i % j != 0 for j in range(2, i))]


# 23. extracts unique elements from a list and stores them in a new list using a list comprehension.
unique_elements = list(set(your_list))


# 24. generates a list of all palindromic numbers up to a specified limit using a list comprehension.
palindromic_numbers = [num for num in range(limit) if str(num) == str(num)[::-1]]

# 25. flatten a nested list using list comprehension.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [item for sublist in nested_list for item in sublist]


# 26. computes the sum of even and odd numbers in a list separately using list comprehension.
even_sum = sum(num for num in your_list if num % 2 == 0)
odd_sum = sum(num for num in your_list if num % 2 != 0)


# 27. generates a list of squares of odd numbers between 1 and 10 using list comprehension.
squares_of_odd = [num**2 for num in range(1, 11) if num % 2 != 0]


# 28. combines two lists into a dictionary using list comprehension.
keys = ['a', 'b', 'c']
values = [1, 2, 3]
combined_dict = {key: value for key, value in zip(keys, values)}


# 29. Develop a program that extracts the vowels from a string and stores them in a list using list comprehension.
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_list = [char for char in your_string if char.lower() in vowels]


# 30. removes all non-numeric characters from a list of strings using list comprehension.
numeric_strings = [''.join(char for char in string if char.isdigit()) for string in your_list]

