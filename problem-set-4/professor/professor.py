import random

def main():
    while True:
        try:
            level = get_level()
            score = 0
            for i in range(10):
                x, y, result = generate_integer(level)
                for j in range(3):
                    try:
                        answer = int(input(f"{x} + {y} = "))
                        if answer == result:
                            score = score+1
                            break
                        else:
                            print("EEE")
                    except ValueError:
                        print("EEE")
                        pass
                    if j == 2:
                            print(f"{x} + {y} = {result}")
            print("Score =", score)
            exit()
        except ValueError:
            pass

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
            else:
                raise ValueError
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    else:
        x = random.randint(10**(level-1), (10**level)-1)
        y = random.randint(10**(level-1), (10**level)-1)
    result = x+y
    return x, y, result

if __name__ == "__main__":
    main()




