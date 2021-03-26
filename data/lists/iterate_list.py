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
    print(f"{i+1}: {temp[i]}")

def run():
  menu()

if __name__ == "__main__":
    run()