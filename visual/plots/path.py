import matplotlib.pyplot as plt

def coordinate():
  x=input("enter value\n")
  y=input("enter seconde value\n")
  return x,y

def path():
  print("retreaving path")
  x_values=[]
  y_values=[]
  for i in range (4):
    data = coordinate()
    x_values.append(data[0])
    y_values.append(data[1])
  return[x_values,y_values]

def run():
  values = path()

  plt.plot(values[0],values[1], "r--o")
  plt.show()

run()