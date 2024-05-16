aString = "Hello!"

aNewString = ""

i = len(aString)

while i > 0:
    
    aNewString += aString[i - 1]
    i -= 1

print('''"''', aString, '''" backwards is "''', aNewString, '''"''', sep='')0