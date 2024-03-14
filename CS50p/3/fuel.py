import math

while True:
    fuel_level = input("Fraction? ")
    try:
        first_num, second_num = fuel_level.split("/")
    except (ValueError):
        continue

    # Check if both variables are digits.
    if first_num.isdigit() and second_num.isdigit():
        # Check if second_num is 0 and ensure first_num not gt second_num
        if int(second_num) != 0 and not (int(first_num) > int(second_num)):
            try:
                fuel_amount = ((int(first_num) / int(second_num)) * 100)
                if 1 < fuel_amount < 99:
                    # Use math module to round down
                    print(f"{math.floor(fuel_amount)}%")
                    break
                elif fuel_amount < 1:
                    print("E")
                    break
                else:
                    print("F")
                    break
            except (ValueError, ZeroDivisionError):
                continue
