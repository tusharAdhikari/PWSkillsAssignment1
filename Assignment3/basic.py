# For Loop Assignment
# Basic Level:
# 1. program to print the numbers from 1 to 10 using a `for` loop.
for num in range(1, 11):
    print(num)


# 2. calculates the sum of all nums in a list using a `for` loop.
your_list = [1, 2, 3, 4, 5]
sum_result = 0
for num in your_list:
    sum_result += num
print(sum_result)

# 3. print the characters of a string in reverse order using a `for` loop.
your_string = "Hello"
for char in reversed(your_string):
    print(char)


# 4. Develop a program that finds the factorial of a given number using a `for` loop.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 5. print the multiplication table of a given number using a `for` loop.
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# 6. counts the number of even and odd numbers in a list using a `for` loop.
your_list = [1, 2, 3, 4, 5]
even_count = 0
odd_count = 0
for num in your_list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Even numbers: {even_count}, Odd numbers: {odd_count}")


# 7. prints the squares of numbers from 1 to 5 using a `for` loop.
for num in range(1, 6):
    square = num ** 2
    print(f"The square of {num} is {square}")

    
# 8. find the length of a string without using the `len()` function.
your_string = "Hello, World!"
length = 0
for char in your_string:
    length += 1
print(length)


# 9.  calculates the average of a list of numbers using a `for` loop.
your_list = [1, 2, 3, 4, 5]
sum_result = 0
for num in your_list:
    sum_result += num
average = sum_result / len(your_list)
print(average)


# 10.prints the first `n` Fibonacci numbers using a `for` loop.
n = 5
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
