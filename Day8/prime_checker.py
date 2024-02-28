def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is a Prime.")
    else:
        print(f"{number} is not a Prime.")

#prime_checker(int(input("Please enter a number: ")))

for x in range(1,101):
    prime_checker(x)