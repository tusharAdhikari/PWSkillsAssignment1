# Question Number 01 to 25

# 1. Create a tuple with integers from 1 to 5.
integer_tuple = (1, 2, 3, 4, 5)

# 2. Access the third element of a tuple.
def access_third_element(tup):
    return tup[2]

# 3. Find the length of a tuple without using the len() function.
def custom_len(tup):
    count = 0
    for _ in tup:
        count += 1
    return count

# 4. Count the occurrences of an element in a tuple.
def count_occurrences(tup, element):
    return tup.count(element)


# 5. Find the index of the first occurrence of an element in a tuple.
def first_index_of_element(tup, element):
    return tup.index(element)

# 6. Check if an element exists in a tuple.
def element_exists(tup, element):
    return element in tup

# 7. Convert a tuple to a list.
def tuple_to_list(tup):
    return list(tup)

# 8. Convert a list to a tuple.
def list_to_tuple(lst):
    return tuple(lst)

# 9. Unpack the elements of a tuple into variables.
def unpack_tuple(tup):
    var1, var2, var3 = tup
    return var1, var2, var3

# 10. Create a tuple of even numbers from 1 to 10.
even_tuple = tuple(range(2, 11, 2))

# 11. Create a tuple of odd numbers from 1 to 10.
odd_tuple = tuple(range(1, 11, 2))

# 12. Concatenate two tuples.
def concatenate_tuples(tup1, tup2):
    return tup1 + tup2

# 13. Repeat a tuple three times.
def repeat_tuple(tup):
    return tup * 3

# 14. Check if a tuple is empty.
def is_empty(tup):
    return len(tup) == 0

# 15. Create a nested tuple.
nested_tuple = ((1, 2), (3, 4), (5, 6))

# 16. Access the first element of a nested tuple.
def access_nested(tup):
    return tup[0][0]

# 17. Create a tuple with a single element.
single_element_tuple = (42,)

# 18. Compare two tuples.
def compare_tuples(tup1, tup2):
    return tup1 == tup2

# 19. Delete a tuple.
# Tuples are immutable, so they cannot be deleted in the traditional sense. They are automatically garbage collected when no longer referenced.

# 20. Slice a tuple.
def slice_tuple(tup, start, end):
    return tup[start:end]

# 21. Find the maximum value in a tuple.
def max_value(tup):
    return max(tup)

# 22. Find the minimum value in a tuple.
def min_value(tup):
    return min(tup)

# 23. Convert a string to a tuple of characters.
def string_to_tuple(s):
    return tuple(s)

# 24. Convert a tuple of characters to a string.
def tuple_to_string(tup):
    return ''.join(tup)

# 25. Create a tuple from multiple data types.
mixed_tuple = (1, 'hello', 3.14, [1, 2, 3], {'a': 1, 'b': 2})

