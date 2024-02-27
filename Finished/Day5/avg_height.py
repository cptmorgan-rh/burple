student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height
print(f"Total Height = {total_height}")

number_students = 0
for student in student_heights:
    number_students += 1
print(f"Number of Students = {number_students}")

print(f"Average Height = {total_height / number_students}")