def main():
    amount = 50

    while amount > 0:
        print(f"Amount Due: {amount}")
        coin = int(input("Insert Coin: "))

        if coin in [25, 10, 5]:
            if coin < amount:
                amount -= coin
            else:
                print(f"Change Owed: {coin -  amount}")
                amount -= coin


main()
