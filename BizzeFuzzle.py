import time 
import replit 

def clear():
  replit.clear()
  
def wait(float):
  time.sleep(float)
  
def init():
  main()
  
def main():
  clear()
  posint = int(input("Gimme a number(ie 1)!"))
  num = posint 
  for char in range(1, (num + 1)):
    if char % 3 == 0:
      char = "Bizzle"
    elif char % 5 == 0:
      char = "Fuzzle"
    else:
      char = char
    print(char)
  x = input("Try Again(y/n)?")
  if x == "y":
    main()
  elif x =="n":
    clear()
    
init()
