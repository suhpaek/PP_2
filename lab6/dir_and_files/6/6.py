import string

def create_text_files():
    for letter in string.ascii_uppercase:
        filename = f"{letter}.txt"
        with open(filename, "w") as file:
            file.write(f"Eto file {filename}\n")
        print(f"Created: {filename}")

create_text_files()