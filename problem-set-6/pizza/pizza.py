import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif not sys.argv[1].endswith(".csv") and len(sys.argv) == 2:
    sys.exit("Not a CSV File")

else:
    try:
        menu = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)

            for row in reader:
                menu.append(row)
                headers = list(row.keys())
        data = [x.values() for x in menu]

        print(tabulate(data, headers, tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")
