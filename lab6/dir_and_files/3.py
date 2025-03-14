import os

def check(path):
    print(f"Checking path: {path}")

    if not os.path.exists(path):
        print("ERROR: Path does not exist")
        return

    print("\nFollowing path exists")

   
    if os.path.isdir(path):
        print(f"\nDirectory name: {os.path.basename(path)}")
        print(f"Directory path: {os.path.abspath(path)}")

       
        print("\nContents of the directory:")
        for entry in os.scandir(path):
            print(f"- {entry.name} ({'Directory' if entry.is_dir() else 'File'})")

    elif os.path.isfile(path):
        print(f"\nFile name: {os.path.basename(path)}")
        print(f"Directory: {os.path.dirname(os.path.abspath(path))}")

path = input("Enter path: ")
check(path)