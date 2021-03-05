#program to count live wires avoided
c=int(input("have many cables I have to avoid? \n"))
a=0
while (c != 0):
  c -= 1
  a +=1
  print("cable avoided")
print("{} cables avoided".format(a))
