while True:
    try:
        fuel = input("Fraction: ")
        x, y = fuel.split("/")
        x = int(x)
        y = int(y)
        result = round(x/y *100)
        if result<=100:
            break
    except (ValueError, ZeroDivisionError):
        pass
    else:
        pass


if 99 <= result <=100:
    print("F")
elif result <= 1:
    print("E")
else:
    print(str(result) + "%")
