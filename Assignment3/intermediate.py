# Intermediate Level:
# 11. check if a given list contains any duplicates using a `for` loop.
def has_duplicates(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False

# 12. prints the prime numbers in a given range using a `for` loop.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_in_range(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)


# 13. counts the number of vowels in a string using a `for` loop.
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

# 14. find the maximum element in a 2D list using a nested `for` loop.
def max_element_2d(matrix):
    max_element = float('-inf')
    for row in matrix:
        for element in row:
            if element > max_element:
                max_element = element
    return max_element


# 15. removes all occurrences of a specific element from a list using a `for` loop.
def remove_element(lst, target):
    for item in lst[:]:  # Using a copy to avoid modifying the list during iteration
        if item == target:
            lst.remove(item)


# 16. generates a multiplication table for numbers from 1 to 5 using a nested `for` loop.
for i in range(1, 6):
    for j in range(1, 11):
        print(i * j, end='\t')
    print()  # Move to the next line for the next multiplier


# 17. converts a list of Fahrenheit temperatures to Celsius using a `for` loop.
def fahrenheit_to_celsius(fahrenheit_list):
    celsius_list = []
    for temp in fahrenheit_list:
        celsius = (temp - 32) * 5/9
        celsius_list.append(celsius)
    return celsius_list


# 18. print the common elements from two lists using a `for` loop.
def common_elements(list1, list2):
    common = []
    for item in list1:
        if item in list2:
            common.append(item)
    return common


# 19. prints the pattern of right-angled triangles using a `for` loop. Use ‘*’ to draw the pattern
for i in range(1, 6):
    print('* ' * i)


# 20. find the greatest common divisor (GCD) of two numbers using a `for` loop.
def gcd(num1, num2):
    smaller = min(num1, num2)
    for i in range(smaller, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i

