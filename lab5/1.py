import re

pattern= r"ab*"

def match(a):
    if re.fullmatch(pattern, a):
        return "Nu est' match"
    else:
        return "Net u tebya match'a :P"
    
text=input("Davai suda svoi string:")
print(match(text))
    

    