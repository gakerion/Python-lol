s = "Education"
vowels = "AEIOUaeiou"
newstring = ""
for i in s:
    if i not in vowels:
        newstring += i
print(newstring)