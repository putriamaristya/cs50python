import random

while True:
    try:
        n = int(input("Level: "))
        if n>0:
            number = random.randint(1,n)
            break
    except ValueError:
            pass

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < number:
                print("Too small!")
                pass
            elif guess > number:
                print("Too large!")
                pass
            else:
                print("Just right!")
                exit()
        else:
            pass
    except ValueError:
        pass
