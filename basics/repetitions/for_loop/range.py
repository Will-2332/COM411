#settings brightenss for beep
levelf=int(input("Set brighteness level \n"))
print("setting levels")
for level in range(0,levelf,2):
  print(level*"*")
print("all set")
