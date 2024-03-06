import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F', 'H']
numbers = ['0', '1', '2', '3', '4', '5']
symbols = ['!', '#', '$']

print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(f"Your password is: {password}")