def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  mini=likelihoods[0]
  maxi=likelihoods[0]
  
  for i in range (len(likelihoods)):
    if mini > likelihoods[i]:
      mini=likelihoods[i]
    if maxi < likelihoods[i]:
      maxi=likelihoods[i]

  return mini,maxi

def run():
  chances=likelihood()
  print(f"Minimum likelihood of falling: {chances[0]}%")
  print(f"Maximum likelihood of falling: {chances[1]}%")

run()