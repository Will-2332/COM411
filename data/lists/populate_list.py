#import directions from iterate_list
#import menu from iterate_list

def directions():
  directions=[]
  directions.append("Move Forward")
  directions.append("Move Backward")
  directions.append("Turn Left")
  directions.append("Turn Right")
  return directions

def menu():
  print("Please select a direction:")
  temp=directions() 
  for i in range(len(temp)):
    print(f"{i}: {temp[i]}") 
  i=int(input()) #using i again, not sure why it worked
  return temp[i]

def run():
  route=[]
  print("Working out escape route...")
  for t in range (5):
    route.append(menu())
  print(route)


run()