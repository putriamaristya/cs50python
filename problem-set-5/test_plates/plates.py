numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
alphabet = ["A", "B", "C", "D", "E", "F",
            "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R",
            "S", "T", "U", "V", "W", "X",
            "Y", "Z"]

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if is_two_letters(s) == True and is_character_right(s) == True and is_sequence_right(s) == True and is_zero(s) == True and is_only_char(s) == True :
        return True
    else:
        return False

def is_two_letters(text):
    r = 0
    for i in text[0:2]:
        if i in alphabet:
            r = r + 1
        else:
            r = 0
    if r != 2:
        return False
    else:
        return True


def is_character_right(text):
    if 2<= len(text) <= 6:
        return True
    else:
        return False

def is_sequence_right(text):
    text_short = text[2:]
    print(text_short)
    x=0
    for i in range(len(text) - 3):
        if text_short[i] in numbers and text_short[i+1] in alphabet:
            return False
        elif text_short[i] in alphabet and text_short[i+1] in numbers:
            x = 1
        elif text_short[i] in numbers and text_short[i+1] in numbers and text_short[i] != "0":
            x = 1
        elif text_short[i] in alphabet and text_short[i+1] in alphabet:
            x = 1
        else:
            return False
    if x == 0:
        return False
    else:
        return True

def is_zero(text):
    for i in range(len(text) - 2):
        if text[i+3] in numbers and text[i+2] == "0":
            return False
        else:
            return True

def is_only_char(text):
    for i in text:
        if i not in numbers and i not in alphabet:
            return False
        else:
            return True

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



if __name__ == "__main__":
    main()