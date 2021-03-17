import random

mini =int(input("Please enter the minimum value:\n"))
maxi =  int(input("Please enter the maximum value:\n"))
rnd = int(random.randrange(mini,maxi))

print("I am thinking of a number between {} and {}. Can you guess what it is?".format(mini,maxi))
n=int(input())

while (n != rnd):
  if (n < rnd):
    print("too low")
    n = int(input("again\n"))
  elif (n > rnd):
    print("too high")
    n = int(input("again\n"))
print("that's right!")