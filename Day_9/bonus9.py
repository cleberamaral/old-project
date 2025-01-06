password = input("Enter new Password :") + "\n"

result = {}
digit = False
upper = False

#check password len
if len(password) >= 8:
    result["Length"] = True
else:
    result["Length"] = False

#check if there is a number
for item in password:
    if item.isdigit():
        digit = True
result["Digit"] = digit

#check if there is Upper
for item in password:
    if item.isupper():
        upper = True
result["Uppercase"] = upper

print(result)
print(result.values())

if all(result.values()): #== True: #it is implicit
    print("Strong Password")
else:
    print("Weak Password")