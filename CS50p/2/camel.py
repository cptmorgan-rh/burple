def main():
    camelcase = input("camelCase: ")
    print(snakecase(camelcase))


def snakecase(input_text):
    snake_case = ""
    for c in input_text:
        if c.isupper():
            snake_case += c.replace(c, f"_{c.lower()}")
        else:
            snake_case += c

    return (f"snake_case: {snake_case}")


main()
