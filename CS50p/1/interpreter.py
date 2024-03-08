equation = input("Expression: ")
first_num, expression, second_num = equation.split(" ")

if expression == "+":
    print(float(first_num) + float(second_num))
elif expression == "-":
    print(float(first_num) - float(second_num))
elif expression == "*":
    print(float(first_num) * float(second_num))
elif expression == "/":
    print(float(first_num) / float(second_num))
