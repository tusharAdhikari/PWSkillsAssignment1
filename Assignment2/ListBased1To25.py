# Question Number 01 to 25

# 1. Create a list with integers from 1 to 10.
integer_list = list(range(1, 11))

# 2. Find the length of a list without using the len() function.
def custom_len(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

# 3. Append an element to the end of a list.
def append_to_list(lst, element):
    lst.append(element)

# 4. Insert an element at a specific index in a list.
def insert_at_index(lst, index, element):
    lst.insert(index, element)

# 5. Remove an element from a list by its value.
def remove_by_value(lst, value):
    lst.remove(value)

# 6. Remove an element from a list by its index.
def remove_by_index(lst, index):
    del lst[index]

# 7. Check if an element exists in a list.
def element_exists(lst, element):
    return element in lst

# 8. Find the index of the first occurrence of an element in a list.
def first_index_of_element(lst, element):
    return lst.index(element)

# 9. Count the occurrences of an element in a list.
def count_occurrences(lst, element):
    return lst.count(element)

# 10. Reverse the order of elements in a list.
def reverse_list(lst):
    return lst[::-1]

# 11. Sort a list in ascending order.
def sort_ascending(lst):
    return sorted(lst)

# 12. Sort a list in descending order.
def sort_descending(lst):
    return sorted(lst, reverse=True)

# 13. Create a list of even numbers from 1 to 20.
even_list = list(range(2, 21, 2))

# 14. Create a list of odd numbers from 1 to 20.
odd_list = list(range(1, 21, 2))

# 15. Find the sum of all elements in a list.
def sum_of_elements(lst):
    return sum(lst)

# 16. Find the maximum value in a list.
def max_value(lst):
    return max(lst)

# 17. Find the minimum value in a list.
def min_value(lst):
    return min(lst)

# 18. Create a list of squares of numbers from 1 to 10.
squares_list = [x ** 2 for x in range(1, 11)]

# 19. Create a list of random numbers.
import random
def random_numbers_list(n):
    return [random.randint(1, 100) for _ in range(n)]

# 20. Remove duplicates from a list.
def remove_duplicates(lst):
    return list(set(lst))

# 21. Find the common elements between two lists.
def common_elements(list1, list2):
    return list(set(list1) & set(list2))

# 22. Find the difference between two lists.
def difference_between_lists(list1, list2):
    return list(set(list1) - set(list2))

# 23. Merge two lists.
def merge_lists(list1, list2):
    return list1 + list2

# 24. Multiply all elements in a list by 2.
def multiply_by_2(lst):
    return [x * 2 for x in lst]

# 25. Filter out all even numbers from a list.
def filter_out_even(lst):
    return [x for x in lst if x % 2 != 0]
