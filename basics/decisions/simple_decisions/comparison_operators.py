n1 = float(input("insert first number : "))
print ("the first number is %.2f" % n1 )
n2 = float(input("insert second number : "))
print ("the second number is %.2f" % n2 )
if (n2 > n1) :
  print ("The first number is the smallest!")
elif (n1 > n2):
  print("The second number is the smallest!")
else :
  print("the numbers are equal")