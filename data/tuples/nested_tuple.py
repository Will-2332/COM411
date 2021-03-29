def steps():
  likelihoods=[("step 1", 50),("step 2", 38),("step 3", 27),("step 4", 99),("step 5", 4)]
  return likelihoods
def run() :
  allsteps=[]
  allsteps=steps()
  bad=[]
  good=[]
  for likelihoods in allsteps:
    if (likelihoods[1]) < 50 :
      good.append(likelihoods)
    else:
      bad.append(likelihoods)
  print(f"Good steps: {len(good)}, Bad steps: {len(bad)}")

run()