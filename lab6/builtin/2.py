def count_case_letters(s):
    upper_case_count = sum(1 for char in s if char.isupper())
    lower_case_count = sum(1 for char in s if char.islower())
    
    print("Uppercase letters:", upper_case_count)
    print("Lowercase letters:", lower_case_count)

input_string = input("Enter a string: ")
count_case_letters(input_string)