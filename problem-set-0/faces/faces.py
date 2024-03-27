def convert(text):
    text = text.replace(':)', '🙂')
    text = text.replace(':(', '🙁')
    return text

def main():
    temp = input("input text: ")
    print(convert(temp))

main()