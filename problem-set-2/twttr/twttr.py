text_in = input("Input: ")
vowels = ["a", "i", "u", "e", "o"]
for i in text_in:
    if i.lower() in vowels:
        None
    else:
        print(i, end="")
print()