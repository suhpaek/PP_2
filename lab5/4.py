import re

pattern= r"\b[A-Z]+[a-z]+\b"

def match(a):
    if re.fullmatch(pattern, a):
        print ("Nu est' match")
        print (f"Vot tvoi result: {re.findall(pattern, a)}")
    else:
        print( "Net u tebya match'a :P")
    
text=input("Davai suda svoi string:")
match(text)
    

    