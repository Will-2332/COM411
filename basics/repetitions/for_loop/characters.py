word=input("Insert the word you want \n")
print("Working")
n=1
for position in range(0, len(word), 1):
    print("index {}".format(n),end=" ")
    print(word[position])
    n+=1
print("Done!")