grocery_list = {}


while True:
    try:
        grocery_item = input().strip().upper()
        if len(grocery_item) != 0:
            if grocery_item in grocery_list:
                grocery_list[grocery_item] += 1
            else:
                grocery_list[grocery_item] = 1
    except (EOFError):
        for k, v in sorted(grocery_list.items()):
            print(f"{v} {k}")
        break
