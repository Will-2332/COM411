#program to count the number of steps missing
def climb_ladder(steps_remaining, steps_crossed):
    if (steps_remaining > steps_crossed):
        print("Still some way to go!")
    else:
        print("We are almost there!") 

steps = int(input("how many steps there are ? \n"))
for total in range(0,steps,1):
  done = steps - total
  climb_ladder(done,total)