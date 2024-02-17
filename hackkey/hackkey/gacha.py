import random

def roll():

  outcome = 0
  gachaRoll = random.randrange(1,100)

  if (gachaRoll > 40):
    outcome = 1
  if (gachaRoll > 70):
    outcome = 2
  if (gachaRoll > 85):
    outcome = 3
  if (gachaRoll > 98):
    outcome = 4
    
  return outcome



