#program to show ascii codes
print("Program Started!")
c=input("Please enter a letter:\n")
while len(c) != 1 :
  print("more than one letter")
  c=input("Please enter a letter:\n")
print("The ASCII code for {} is: {}".format(c,ord(c)))
print("Program Ended!")