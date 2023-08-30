# Question Number 26 to 50

# 26. Check if two tuples are identical.
def are_tuples_identical(tup1, tup2):
    return tup1 == tup2

# 27. Sort the elements of a tuple.
def sort_tuple(tup):
    return tuple(sorted(tup))

# 28. Convert a tuple of integers to a tuple of strings.
def convert_int_tuple_to_str(tup):
    return tuple(str(x) for x in tup)

# 29. Convert a tuple of strings to a tuple of integers.
def convert_str_tuple_to_int(tup):
    return tuple(int(x) for x in tup)

# 30. Merge two tuples.
def merge_tuples(tup1, tup2):
    return tup1 + tup2

# 31. Flatten a nested tuple.
def flatten_tuple(nested_tuple):
    flattened = ()
    for item in nested_tuple:
        if isinstance(item, tuple):
            flattened += flatten_tuple(item)
        else:
            flattened += (item,)
    return flattened

# 32. Create a tuple of the first 5 prime numbers.
def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
        num += 1
    return tuple(primes)

first_5_primes = generate_primes(5)

# 33. Check if a tuple is a palindrome.
def is_tuple_palindrome(tup):
    return tup == tup[::-1]

# 34. Create a tuple of squares of numbers from 1 to 5.
squares_tuple = tuple(x ** 2 for x in range(1, 6))

# 35. Filter out all even numbers from a tuple.
def filter_out_even(tup):
    return tuple(x for x in tup if x % 2 != 0)

# 36. Multiply all elements in a tuple by 2.
def multiply_by_2(tup):
    return tuple(x * 2 for x in tup)

# 37. Create a tuple of random numbers.
import random
def random_numbers_tuple(n):
    return tuple(random.randint(1, 100) for _ in range(n))

# 38. Check if a tuple is sorted.
def is_tuple_sorted(tup):
    return all(tup[i] <= tup[i+1] for i in range(len(tup)-1))

# 39. Rotate a tuple to the left by n positions.
def rotate_left(tup, n):
    n = n % len(tup)
    return tup[n:] + tup[:n]

# 40. Rotate a tuple to the right by n positions.
def rotate_right(tup, n):
    n = n % len(tup)
    return tup[-n:] + tup[:-n]

# 41. Create a tuple of the first 5 Fibonacci numbers.
def generate_fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return tuple(fib)

first_5_fibonacci = generate_fibonacci(5)

# 42. Create a tuple from user input.
def input_to_tuple():
    user_input = input("Enter elements separated by commas: ")
    elements = user_input.split(',')
    return tuple(elements)

# 43. Swap two elements in a tuple.
def swap_elements(tup, index1, index2):
    lst = list(tup)
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return tuple(lst)

# 44. Reverse the elements of a tuple.
def reverse_tuple(tup):
    return tup[::-1]

# 45. Create a tuple of the first n powers of 2.
def powers_of_2(n):
    return tuple(2 ** i for i in range(n))


# 46. Find the longest string in a tuple of strings.
def longest_string_in_tuple(tup):
    return max(tup, key=len)

# 47. Find the shortest string in a tuple of strings.
def shortest_string_in_tuple(tup):
    return min(tup, key=len)

# 48. Create a tuple of the first n triangular numbers.
def triangular_numbers(n):
    return tuple((i * (i + 1)) // 2 for i in range(1, n + 1))

# 49. Check if a tuple contains another tuple as a subsequence.
def has_subsequence(tup, subseq):
    n, m = len(tup), len(subseq)
    if m == 0:
        return True
    if n == 0:
        return False
    
    i, j = 0, 0
    while i < n and j < m:
        if tup[i] == subseq[j]:
            j += 1
        i += 1
    return j == m

# 50. Create a tuple of alternating 1s and 0s of length n.
def alternating_ones_zeros(n):
    return tuple(1 if i % 2 == 0 else 0 for i in range(n))
