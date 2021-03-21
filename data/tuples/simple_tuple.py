def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  mini=likelihoods[0]
  for i in range (len(likelihoods)):
    if mini > likelihoods[i]:
      mini=likelihoods[i]

  return mini

def run():
  print(f"Minimum likelihood of falling: {likelihood()}%")

run()