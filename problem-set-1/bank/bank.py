greeting = input("Greeting: ")

if greeting.casefold().strip().startswith("hello"):
    print("$0")
elif greeting.casefold().strip().startswith("h"):
    print("$20")
else:
    print("$100")