#code to show an ascii character from the number
print("Program Started!")
code=int(input("Please enter an ASCII code:\n"))
if code in range (32,127,1) :
  print("The character represented by the ASCII code {} is: {}".format(code,chr(code)))
else :
  print("wronge value")
print("Program Ended!")