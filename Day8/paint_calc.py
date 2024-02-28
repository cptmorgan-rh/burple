import math

def paint_calc(height, width, cover):
    return math.ceil((height * width) / cover)

test_h = int(input("Please enter the height of the wall: "))
test_w = int(input("Please enter the width of the wall: "))
coverage = 5
print(f"You'll need {paint_calc(height=test_h, width=test_w, cover=coverage)} cans of paint")