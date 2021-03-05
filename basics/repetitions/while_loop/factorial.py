#factorial
import math
n=int(input("insert your number \n"))
print(math.factorial(n))
t =0
while n >= 1 :
  t += n*(n-1)
print("the result is {}".format(t))