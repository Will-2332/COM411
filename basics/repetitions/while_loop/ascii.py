#program to fill battery bars
level=int(input("how many bars should I fill?\n"))
bars=0
while level != 0 :
  level -= 1
  bars += 1
  print("chargin battery", end=" ")
  print("\u275A"*bars)
print("battery charged")