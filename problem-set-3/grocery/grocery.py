groceries = {}
while True:
    try:
        item = input()
        if item in groceries:
            n = int(groceries.get(item))
            groceries[item] = n+1
        else:
            groceries[item] = 1
    except KeyError:
        pass
    except EOFError:
        print("\n", end="")
        break

groceries = dict(sorted(groceries.items()))
for item in groceries:
    print(str(groceries[item]) + " " + item.upper())
