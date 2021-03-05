n=int(input("How many numbers should I sum up?\n"))
t =0
s =0
c = 0
while n != 0 :
  c +=1
  s = int(input("enter {} number\n".format(c)))
  t += s
  n -= 1

print("the answer is {}".format(t))