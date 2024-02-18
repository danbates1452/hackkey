import random

def roll():

  outcome = 0
  gachaRoll = random.randrange(1,100)

  if (gachaRoll > 98):
    outcome = 4
  elif (gachaRoll > 85):
    outcome = 3
  elif (gachaRoll > 70):
    outcome = 2
  elif (gachaRoll > 40):
    outcome = 1

  return outcome



