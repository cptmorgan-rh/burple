import os


def calculate_nums(first_num, second_num, expression):

    if expression == "+":
        return (float(first_num) + float(second_num))
    elif expression == "-":
        return (float(first_num) - float(second_num))
    elif expression == "*":
        return (float(first_num) * float(second_num))
    elif expression == "/":
        return (float(first_num) / float(second_num))


def calculator():
    first_num = input("What's the first number? ")
    print("Pick an expression: + - * /")
    expression = input()
    second_num = input("What's the second number? ")
    result = calculate_nums(first_num, second_num, expression)
    while True:
        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == 'y':  # noqa E501
            first_num = result
            print("Pick an expression: + - * /")
            expression = input()
            second_num = input("What's the second number? ")
            result = calculate_nums(first_num, second_num, expression)
        else:
            break
    os.system('clear')
    calculator()


calculator()
