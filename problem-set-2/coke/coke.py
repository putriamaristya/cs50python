print("Amount Due: 50")
amount_due = 50

while True:
    coin_inserted = int(input("Insert Coin: "))
    if coin_inserted == 5 or coin_inserted == 10 or coin_inserted == 25:
        amount_due = amount_due - coin_inserted
        if amount_due > 0:
            print("Amount Due:",  amount_due)
        elif amount_due < 0:
            print("Change Owed:",  abs(amount_due))
            break
        elif amount_due == 0:
            print("Change Owed:", amount_due)
            break
    else:
        print("Amount Due:", amount_due)