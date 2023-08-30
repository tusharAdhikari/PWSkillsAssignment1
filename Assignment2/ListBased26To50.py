# Question Number 26 to 50

# Question26. Convert a list of strings to a list of integers.
stringList = ["1", "2", "3", "4", "5"]
intList = [int(num) for num in stringList]
print(intList)
 
# Question27. Convert a list of integers to a list of strings.
stringList = [str(num) for num in intList]
print(stringList)
 
# Question28. Flatten a nested list.
nestedList = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattenedList = [num for sublist in nestedList for num in sublist]
print(flattenedList)

# Question29. Create a list of the first 10 Fibonacci numbers.
fibTenList = list()
for i in range(11):
    if i == 0:
        fibTenList.append(i)
    if i == 1 or i == 2:
        fibTenList.append(i)
    
    fibTenList.append(i + (i - 1))
    
# Question 30. Check if a list is sorted.
def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

# Question 31. Rotate a list to the left by n positions.
def rotate_left(lst, n):
    n = n % len(lst)
    return lst[n:] + lst[:n]

# Question 32. Rotate a list to the right by n positions.
def rotate_right(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]

# Question 33. Create a list of prime numbers up to 50.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def prime_numbers_up_to_50():
    return [num for num in range(2, 51) if is_prime(num)]

# Question 34. Split a list into chunks of size n.
def split_into_chunks(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

# Question 35. Find the second largest number in a list.
def second_largest(lst):
    if len(lst) < 2:
        return None
    sorted_lst = sorted(lst, reverse=True)
    return sorted_lst[1]

# Question 36. Replace every element in a list with its square.
def square_elements(lst):
    return [x ** 2 for x in lst]

# Question 37. Convert a list to a dictionary where list elements become keys and their indices become values.
def list_to_dict(lst):
    return {value: index for index, value in enumerate(lst)}

# Question 38. Shuffle the elements of a list randomly.
import random
def shuffle_list(lst):
    shuffled = lst.copy()
    random.shuffle(shuffled)
    return shuffled

# Question 39. Create a list of the first 10 factorial numbers.
import math
def factorial_numbers(n):
    return [math.factorial(i) for i in range(1, n + 1)]

# Question 40. Check if two lists have at least one element in common.
def has_common_element(lst1, lst2):
    return any(x in lst2 for x in lst1)

# Question 41. Remove all elements from a list.
def remove_all_elements(lst):
    lst.clear()

# Question 42. Replace negative numbers in a list with 0.
def replace_negatives_with_zero(lst):
    return [x if x >= 0 else 0 for x in lst]

# Question 43. Convert a string into a list of words.
def string_to_word_list(s):
    return s.split()

# Question 44. Convert a list of words into a string.
def word_list_to_string(lst):
    return ' '.join(lst)

# Question 45. Create a list of the first n powers of 2.
def powers_of_2(n):
    return [2 ** i for i in range(n)]

# Question 46. Find the longest string in a list of strings.
def longest_string(lst):
    return max(lst, key=len)

# Question 47. Find the shortest string in a list of strings.
def shortest_string(lst):
    return min(lst, key=len)

# Question 48. Create a list of the first n triangular numbers.
def triangular_numbers(n):
    return [(i * (i + 1)) // 2 for i in range(1, n + 1)]

# Question 49. Check if a list contains another list as a subsequence.
def has_subsequence(lst, subseq):
    n, m = len(lst), len(subseq)
    if m == 0:
        return True
    if n == 0:
        return False
    
    i, j = 0, 0
    while i < n and j < m:
        if lst[i] == subseq[j]:
            j += 1
        i += 1
    return j == m

# Question 50. Swap two elements in a list by their indices.
def swap_elements(lst, index1, index2):
    lst[index1], lst[index2] = lst[index2], lst[index1]
