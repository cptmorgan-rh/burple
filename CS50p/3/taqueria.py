menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

order_total: float = 0.00

while True:
    try:
        menu_item = input("Item: ")
        if menu_item.title() in menu:
            order_total += menu[menu_item.title()]
            print(f"Total: ${order_total:.2f}")
    except (EOFError):
        print("\n")
        break
