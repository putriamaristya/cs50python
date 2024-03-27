import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif not sys.argv[1].endswith(".py") and len(sys.argv) == 2:
    sys.exit("Not a Python File")

else:
    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()


        lines_fin = []
        for line in lines:
            line_temp = line.lstrip()
            if (line_temp.startswith("#") == True or line_temp == "\n") or line_temp == "":
                None
            else:
                lines_fin.append(line_temp)
        print(len(lines_fin))
    except FileNotFoundError as e:
        print("File does not exist")





