rows=int(input("How many rows should I have?\n"))
columns=int(input("How many columns should I have?\n"))
 
print("Here I go:")
for count in range(0, rows, 1):
  for number in range(0, columns, 1):
        print(":-)", end="")
  print("")

print("Done!")