import math 
import replit 
from collections import Counter

def clear():
  replit.clear()
  
def init():
  clear()
  main()
  
def main():
  print("[1]Pythagorean Theorem\n[2]Statistics & Probability\n[3]Graphs & Tables\n[4]Number Sequences")
  mainop = input()
  if mainop == "1":
    pytheorem()
  elif mainop == "2":
    statprob()
  elif mainop == "3":
    graphtable()
  elif mainop == "4":
    numseq()
  else:
    main()
    
def pytheorem():
  clear()
  print("[1]Find Hypotenuse Length\n[2]Find Missing Leg Length")
  pyop = input()
  if pyop == "1":
    clear()
    leglength = input("Type Both Leg Lengths(Separated by a Dash and Space(ie 1-3)>\n")
    if "-" in leglength:
      nums = leglength.split('-')
      int1 = int(nums[0])
      int2 = int(nums[1])
      x = (int1**2 + int2**2)
      clear()
      print("Legs: " + str(int1) + ", " + str(int2) + "\nHypotenuse: " + str(math.sqrt(x)) + "\n")
      main()
    else:
      pyop()
  elif pyop == "2":
    clear()
    hylength = float(input("Hypotenuse Length: "))
    leglength = float(input("Leg Length: "))
    x = (hylength**2 - leglength**2)
    print("Missing Leg Length: " + str(math.sqrt(x)) + "\n")
    main()
    
def statprob():
  clear()
  print("[1]Find the mode/mean/median/MAD\n[2]Calculate Probability")
  statop = input()
  if statop == "1":
    x = input("Please Input Your Sequence of Numbers(Separated by dashes[1-2-3]) > \n")
    sequence = x.split('-')
    
    
init()
#pytheorem()
