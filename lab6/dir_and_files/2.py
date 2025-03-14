import os

def check(path):
	print(f"Checkaem est' li access{path}\n")

	if os.path.exists(path):
		print("Path est'")
	else:
		print("ERROR net tvoego path'a")
		return
	
	if os.path.isfile(path):
		print("Path eto file")
	elif os.path.isdir(path):
		print("Path eto directoriya")

	if os.access(path, os.W_OK):
		print("V path mozhno napisat'")
	else:
		print("ERROR nel'zya nichego pisat', u nas totalitarism")

	if os.access(path, os.R_OK):
		print("Path mozhno prochitat'")
	else:
		print("ERROR nel'zya nichego chitat', u nas totalitarism")

	if os.access(path, os.X_OK):
		print("Path mozhno vipolnit'")
	else:
		print("ERROR nel'zya nichego vipolnit', u nas totalitarism")

path = input("VVodi svoi path: ")
check(path)