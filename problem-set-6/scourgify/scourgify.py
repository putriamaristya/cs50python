import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 4:
    sys.exit("Too many command-line arguments")

elif not sys.argv[1].endswith(".csv") and len(sys.argv) == 3:
    sys.exit(f"Could not read {sys.argv[1]}")

else:
    try:
        students = []
        names = []
        houses = []
        #open csv and create names and houses dictionary
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for name, house in reader:
                names.append({"name": name})
                houses.append({"house": house})

        #separate first and last name
        for name in names[1:]:
            last, first = name["name"].rstrip().split(",")
            name_temp = {"first":first.lstrip(), "last":last}
            students.append(name_temp)

        #combine names and houses dictionary
        for i in range(len(students)):
            students[i].update(houses[i+1])

        #write csv
        with open(sys.argv[2], "w", newline='') as output_file:
            writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            writer.writerows(students)

    except FileNotFoundError:
        sys.exit("File does not exist")
