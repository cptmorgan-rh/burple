print("""
Welcome to Treasure Island\n.
Your mission is to find the treasure.""")
direction = input("Do you wan to go left or right? ").lower()

if direction == "left":
    action = input("You come to a heavy flowing river. Do you want to swim across or wait? ").lower()
    if action == "wait":
        door = input("After waiting the river calms and you come to three doors. One Red, one Blue, and one Yellow. Which do you enter? ").lower()
        if door == "yellow":
            print("You win!")
        else:
            print("Game Over.")
    else:
        print("Game Over.")
else:
    print("Game Over.")