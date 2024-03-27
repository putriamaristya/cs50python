#install pyfiglet
#pip install pyfiglet

import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
f = figlet.getFonts()

if len(sys.argv) == 3:
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in f:
        text = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print("Output:\n", figlet.renderText(text), sep="")
    else:
        sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    text = input("Input: ")
    f = figlet.getFonts()
    figlet.setFont(font=random.choice(f))
    print("Output:\n", figlet.renderText(text), sep="")
else:
    sys.exit("Invalid usage")

