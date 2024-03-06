print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()

true_count = 0
love_count = 0

for x in "true":
    true_count += name1.count(x)
    true_count += name2.count(x)

for x in "love":
    love_count += name1.count(x)
    love_count += name2.count(x)

love_score = int(str(true_count) + str(love_count))


if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")