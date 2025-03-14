def count_lines(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            line_count = sum(1 for line in file)
        print(f"Total number of lines: {line_count}")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

filename = input("Enter the file path: ")
count_lines(filename)
