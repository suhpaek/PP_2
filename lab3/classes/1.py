class string:
    def getString(self):
        self.s = str(input("Enter a string: "))
    
    def printString(self):
        print(self.s.upper())

str1 = string()
str1.getString()
str1.printString()