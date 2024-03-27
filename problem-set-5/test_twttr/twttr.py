def main():
    text_in = input("Input: ")
    print(shorten(text_in))


def shorten(word):
    text_out = str()
    vowels = ["a", "i", "u", "e", "o"]
    for i in word:
        if i.lower() in vowels:
            None
        else:
            text_out = text_out+i
    return text_out


if __name__ == "__main__":
    main()

