# Question Number 01 to 25

# 1. Create a set with integers from 1 to 5.
integer_set = {1, 2, 3, 4, 5}

# 2. Add an element to a set.
def add_to_set(s, element):
    s.add(element)

# 3. Remove an element from a set.
def remove_from_set(s, element):
    s.remove(element)

# 4. Check if an element exists in a set.
def element_exists(s, element):
    return element in s

# 5. Find the length of a set without using the len() function.
def custom_len(s):
    count = 0
    for _ in s:
        count += 1
    return count

# 6. Clear all elements from a set.
def clear_set(s):
    s.clear()

# 7. Create a set of even numbers from 1 to 10.
even_set = {x for x in range(2, 11, 2)}

# 8. Create a set of odd numbers from 1 to 10.
odd_set = {x for x in range(1, 11, 2)}

# 9. Find the union of two sets.
def union_sets(set1, set2):
    return set1.union(set2)

# 10. Find the intersection of two sets.
def intersection_sets(set1, set2):
    return set1.intersection(set2)

# 11. Find the difference between two sets.
def difference_sets(set1, set2):
    return set1.difference(set2)

# 12. Check if a set is a subset of another set.
def is_subset(set1, set2):
    return set1.issubset(set2)

# 13. Check if a set is a superset of another set.
def is_superset(set1, set2):
    return set1.issuperset(set2)

# 14. Create a set from a list.
def list_to_set(lst):
    return set(lst)

# 15. Convert a set to a list.
def set_to_list(s):
    return list(s)

# 16. Remove a random element from a set.
import random
def remove_random_element(s):
    if s:
        random_element = random.choice(list(s))
        s.remove(random_element)

# 17. Pop an element from a set.
def pop_from_set(s):
    if s:
        return s.pop()

# 18. Check if two sets have no elements in common.
def no_common_elements(set1, set2):
    return set1.isdisjoint(set2)

# 19. Find the symmetric difference between two sets.
def symmetric_difference_sets(set1, set2):
    return set1.symmetric_difference(set2)

# 20. Update a set with elements from another set.
def update_set(set1, set2):
    set1.update(set2)

# 21. Create a set of the first 5 prime numbers.
prime_set = {2, 3, 5, 7, 11}

# 22. Check if two sets are identical.
def are_sets_identical(set1, set2):
    return set1 == set2

# 23. Create a frozen set.
frozen = frozenset({1, 2, 3, 4, 5})

# 24. Check if a set is disjoint with another set.
def is_disjoint(set1, set2):
    return set1.isdisjoint(set2)

# 25. Create a set of squares of numbers from 1 to 5.
squares_set = {x ** 2 for x in range(1, 6)}