def is_palindrome(s):
    return s == s[::-1]

input_string = input("Enter a string: ")
print("Is palindrome:", is_palindrome(input_string))