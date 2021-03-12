def cross_bridge (steps):
  if steps >= 5 :
    for step in range (3,steps,1):
      print ("Crossed step. \nThe bridge is collapsing!")
    for step in range (0,3,1):
      print ("Crossed step. \nWe must keep going!")
  else :
    for step in range (0,steps,1):
      print ("Crossed step. \nWe must keep going!")

steps = int(input("number of steps? \n"))
cross_bridge (steps)