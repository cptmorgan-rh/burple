print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
percentage = int(input("What percentage tp would you like to give? 10, 12, or 15? "))
total_people = int(input("How many people to split the bill? "))
per_person = round((total_bill + (total_bill * percentage/100)) / total_people, 2)
final_amount = "{:.2f}".format(per_person)
print(f"Each person should pay: ${final_amount}")