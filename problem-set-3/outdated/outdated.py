months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

while True:
    try:
        date = input("Date: ").strip()
        if "/" in date:
            m,d,y = date.split("/")
            m = int(m)
            d = int(d)
            if d<=31 and m<=12:
                print(y, "-", f"{m:02}", "-", f"{d:02}", sep="")
                break
            else:
                pass
        elif any(item in date for item in months) and "," in date:
            m,d,y = date.split(" ")
            m = months.index(m) + 1
            d = int(d.removesuffix(","))
            if d<=31 and m<=12:
                print(y, "-", f"{m:02}", "-", f"{d:02}", sep="")
                break
            else:
                pass
    except:
        pass
