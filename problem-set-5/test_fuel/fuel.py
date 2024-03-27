def main():
    fuel = input("Fraction: ")
    frctn = convert(fuel)
    print(gauge(frctn))


def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            out = round((x/y)*100)
            if out <= 100:
                break
        except (ValueError, ZeroDivisionError):
            pass
        else:
            pass
    return out


def gauge(percentage):
    if 99 <= percentage <= 100:
        return ("F")
    elif percentage <= 1:
        return ("E")
    else:
        return (str(percentage) + "%")


if __name__ == "__main__":
    main()






