#program to count how many odds or even numbers there is
even=0
odds=0
n1 = float(input("insert first number :"))
if (n1 % 2 != 0) :
  odds= odds + 1
else :
  even = even + 1
n2 = float(input("insert second number :"))
if (n2 % 2 == 0) :
  even = even + 1
else :
  odds += 1
n3 = float(input("insert third number :"))
if (n3 % 2 == 0) :
  even +=  1
else :
  odds = odds + 1
print("number of odds :",format(odds))
print("number of evens :",format(even))