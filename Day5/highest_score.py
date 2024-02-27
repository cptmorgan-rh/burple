student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

highest_score = 0
for x in student_scores:
    print(x)
    if x > highest_score:
        highest_score = x

print(f"{highest_score} is the highest score.")