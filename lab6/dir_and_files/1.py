import os

def list_contents(path):
    try:
        directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        print("\nDirectories:")
        for d in directories:
            print(d)

        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        print("\nFiles:")
        for f in files:
            print(f)

        print("\nAll Directories and Files:")
        for item in os.listdir(path):
            print(item)

    except FileNotFoundError:
        print("The specified path does not exist.")
    except PermissionError:
        print("Permission denied to access the specified path.")

path = input("Enter the path to list contents: ")
list_contents(path)