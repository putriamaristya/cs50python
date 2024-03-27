def main():
    what_time = input("What time is it? ")

    if 7 <= convert(what_time) <= 8:
        print("breakfast time")
    elif 12 <= convert(what_time) <= 13:
        print("lunch time")
    elif 18 <= convert(what_time) <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)

    if 0 <= minutes < 60:
        x = minutes/60

    return hours + x


if __name__ == "__main__":
    main()