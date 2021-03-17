#program to call multiple defs
def sum_weights(x,y):
  tw = x+y
  return tw
def calc_avg_weight(x,y):
  aw = (x+y)/2
  return aw
def run():
  x=float(input("What is the weight of Beep??\n"))
  y=float(input("What is the weight of Bop?\n"))
  choice =input("What would you like to calculate (sum or average)?\n type exit to finish\n")

  if (choice.lower() == "sum"):
    answer=sum_weights(x,y)
    print ("The sum of Beep and Bop's weight is {}".format(answer))
  elif (choice.lower() == "average"):
    answer=calc_avg_weight(x,y)
    print ("The average of Beep and Bop's weight is {}".format(answer))

run()