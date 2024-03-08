def main():
    amount = 50
    accepted_currency = [25, 10, 5]

    print("Amount Due: 50")

    while amount > 0:
        coin = int(input("Insert Coin: "))

        if coin in accepted_currency:
            if coin < amount:
                amount -= coin
                print(f"Amount Due: {amount}")
            else:
                print(f"Change Owed: {coin -  amount}")
                amount -= coin


main()
