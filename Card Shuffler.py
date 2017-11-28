import time 
import replit
import random

regdec = ["Ace of Spades", "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades", "7 of Spades", "8 of Spades", "9 of Spades", "10 of Spades", "Jack of Spades", "Queen of Spades", "King of Spades", "Ace of Diamonds", "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds", "6 of Diamonds", "7 of Diamonds", "8 of Diamonds", "9 of Diamonds", "10 of Diamonds", "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds"]

def wait(float):
  time.sleep(float)

def clear():
  replit.clear()
  
def init():
  main()
  
def main():
  clear()
  while True:
    shuffdec = random.sample(regdec, 10)
    shuffdec = '\n'.join(shuffdec)
    x = input("Deal(y/n)?")
    if x == "y":
      print("\nYour Cards:\n" + str(shuffdec))
      again = input("\nnAgain(y/n)?")
      if again == "y":
        main()
      elif again == "n":
        break
    elif x == "n":
      print("Bye")
      break
    else:
      main()
  clear()
    
init()
