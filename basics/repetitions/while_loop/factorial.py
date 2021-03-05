#factorial
n=int(input("insert your number \n"))
t =1
c=0
while c < n :
  c += 1
  t = t * c
print("the result is {}".format(t))