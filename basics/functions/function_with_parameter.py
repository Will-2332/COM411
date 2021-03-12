def escape_by(option) :
  if option.lower() == "jumping over":
    print ("We cannot escape that way! \nThe boulder is too big!")
  elif option.lower() == "running around" :
    print ("We cannot escape that way! \nThe boulder is moving too fast!")
  elif option.lower() == "going deeper" :
    print ("That might just work! \nLet's go deeper!")
  else :
    print("that's not a plan!")

option = input("what should we do?\n")
escape_by(option)