print("Towards which direction should I paint (up, down, left or right)?")
dir = str(input())



if (dir == "up" or dir == "Up" or dir == "UP" or dir == "uP"):
    print("I am painting in the upward direction!")
elif (dir == "Down" or dir == "DOWN" or dir == "down"):
    print("I am painting in the downward direction!")
elif (dir == "left" or dir == "Left" or dir == "LEFT"):
    print("I am painting in the leftwards direction!")
elif (dir == "right" or dir == "Right" or dir == "RIGHT"):
    print("I am painting in the right direction!")
else:
    print("that's not a direction")