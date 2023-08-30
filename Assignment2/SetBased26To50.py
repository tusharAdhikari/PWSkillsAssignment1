# Question Number 26 to 50

# 26. Filter out all even numbers from a set.
def filter_out_even(s):
    return {x for x in s if x % 2 != 0}

# 27. Multiply all elements in a set by 2.
def multiply_elements_by_2(s):
    return {x * 2 for x in s}

# 28. Create a set of random numbers.
import random
def random_numbers_set(n):
    return {random.randint(1, 100) for _ in range(n)}

# 29. Check if a set is empty.
def is_set_empty(s):
    return len(s) == 0

# 30. Create a nested set (hint: use frozenset).
nested_set = {frozenset({1, 2}), frozenset({3, 4})}

# 31. Remove an element from a set using the discard method.
def remove_element(s, element):
    s.discard(element)

# 32. Compare two sets.
def compare_sets(set1, set2):
    return set1 == set2

# 33. Create a set from a string.
def string_to_set(s):
    return set(s)

# 34. Convert a set of strings to a set of integers.
def convert_str_set_to_int(s):
    return {int(x) for x in s}

# 35. Convert a set of integers to a set of strings.
def convert_int_set_to_str(s):
    return {str(x) for x in s}

# 36. Create a set from a tuple.
def tuple_to_set(tup):
    return set(tup)

# 37. Convert a set to a tuple.
def set_to_tuple(s):
    return tuple(s)

# 38. Find the maximum value in a set.
def max_value_in_set(s):
    return max(s)

# 39. Find the minimum value in a set.
def min_value_in_set(s):
    return min(s)

# 40. Create a set from user input.
def input_to_set():
    user_input = input("Enter elements separated by spaces: ")
    elements = user_input.split()
    return set(elements)

# 41. Check if the intersection of two sets is empty.
def intersection_empty(set1, set2):
    return not set1.intersection(set2)

# 42. Create a set of the first 5 Fibonacci numbers.
def generate_fibonacci_set(n):
    fib = {0, 1}
    while len(fib) < n:
        next_fib = sum(fib)
        fib.add(next_fib)
    return fib

# 43. Remove duplicates from a list using sets.
def remove_duplicates_with_set(lst):
    return list(set(lst))

# 44. Check if two sets have the same elements, regardless of their count.
def same_elements(set1, set2):
    return set1 == set2

# 45. Create a set of the first n powers of 2.
def powers_of_2_set(n):
    return {2 ** i for i in range(n)}

# 46. Find the common elements between a set and a list.
def common_elements_set_list(s, lst):
    return s.intersection(lst)

# 47. Create a set of the first n triangular numbers.
def triangular_numbers_set(n):
    return {(i * (i + 1)) // 2 for i in range(1, n + 1)}

# 48. Check if a set contains another set as a subset.
def contains_subset(main_set, subset):
    return subset.issubset(main_set)

# 49. Create a set of alternating 1s and 0s of length n.
def alternating_ones_zeros_set(n):
    return {(i % 2) for i in range(n)}

# 50. Merge multiple sets into one.
def merge_multiple_sets(*sets):
    merged_set = set()
    for s in sets:
        merged_set.update(s)
    return merged_set
