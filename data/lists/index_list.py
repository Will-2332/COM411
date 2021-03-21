def movements():
  path=[]
  path.append("Move Forward")
  path.append(10)
  path.append("Move Backward")
  path.append(5)
  path.append("Move Left")
  path.append(3)
  path.append("Move Right")
  path.append(1)
  return path
def run():
  print("Mooooving")
  path = movements()
  print(f"{path[0]} for {path[1]} steps")
  print(f"{path[2]} for {path[3]} steps")
  print(f"{path[4]} for {path[5]} steps")

run()