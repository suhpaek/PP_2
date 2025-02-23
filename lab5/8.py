import re

pattern= r"(?=[A-Z])"

def match(a):
    split= re.split(pattern, text)
    
    print(split)
    
text=input("Davai suda svoi string:")
match(text)
    
