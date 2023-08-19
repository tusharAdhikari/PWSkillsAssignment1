# Question4: Check the String is Palindrome or not

string = input("Enter a string: ")
# Remove spaces and convert to lowercase for comparison
cleaned_string = string.replace(" ", "").lower()
reversed_string = cleaned_string[::-1]

if cleaned_string == reversed_string:
    print("The input string is a palindrome.")
else:
    print("The input string is not a palindrome.")