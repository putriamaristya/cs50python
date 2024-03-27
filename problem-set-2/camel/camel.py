text = input("camelCase: ")

for i in text:
    if i == i.upper():
        print("_" + i.lower(), end="")
    else:
        print(i, end="")
print()
