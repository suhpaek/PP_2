inp = inp = r"C:\Users\ASUS\PP_2\lab6\dir_and_files\e7task\est.txt"
out = 'output.txt'

data = []

with open(inp, 'r') as file:
	data = file.readlines()

with open(out, 'w') as file:
	for i in data:
		file.writelines(i)
	