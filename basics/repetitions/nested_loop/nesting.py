#program to count distance beetwen markers
sequence = input("Please enter a sequence\n")

marker = input("Please enter the character for the marker\n")

counting = False
count = -1
 
for letter in sequence :
  if (counting == False and letter == marker ):
    counting = True
  elif (counting ):
    count +=1

print ("The distance between the markers is", format(count))