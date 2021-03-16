#program to print a ladder
def display_ladder(steps):
  print("***\n| |")


def create_ladder():
  number=int(input("how many steps remain ?\n"))
  for i in range (0,number,1):
    display_ladder(number)

create_ladder()
