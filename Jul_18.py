# takes in a number and lets the user guess the number till they get it right.abs

import random

for x in range(1):
    rando = random.randint(1,11)

def guess():
  user_guess = int(input("guess a number between 1 and 10: "))
  
  if rando == user_guess:
    print("You were right!")   
  else:
    print("nope, try again")
    guess()

guess()
