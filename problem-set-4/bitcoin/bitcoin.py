#install requests

import requests
import sys

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
jsn = response.json()

conv = jsn["bpi"]["USD"]["rate"]
conv = float(conv.replace(",", ""))

try:
    i = float(sys.argv[1])
    amount = conv*i
    print(f"${amount:,.4f}")
except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")