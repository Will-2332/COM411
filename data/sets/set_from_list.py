def observed():
  observations=[]
  for i in range (6):
    temp=input("add an item to the list\n")
    observations.append(temp)
  return observations

def run():
  print(f"Counting observations")
  observations=observed()
  observations_set = set()
  for observation in observations:
    data = (observation, observations.count(observation))
    observations_set.add(data)
  for data in observations_set:
    print(f"{data[0]} observed {data[1]} times.")

if "__main__":
  run()
