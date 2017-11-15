from math import pi 
import replit
import time 

def clear():
  replit.clear()

def wait(float):
  time.sleep(float)
  
def main():
  clear()
  global a 
  a = float(input("Radius of Circle or Sphere: "))
  if a != "":
    clear()
    choice()
  elif a == "":
    error()
    
def choice():
  print("Radius: " + str(a))
  print("Would you like to find: \n[1]Circumference(Circle)\n[2]Area(Circle)\n[3]Surface Area(Sphere)\n[4]Volume(Sphere)\n[5]Enter a New Radius\n[6]Done")
  b = input("")
  if b == "1":
    circumference()
    clear()
    print("Circumference: " + str(cir))
    choice()
  elif b == "2":
    area()
    clear()
    print("Area: " + str(ar))
    choice()
  elif b == "3":
    surfacearea() 
    clear()
    print("Surface Area: " + str(surface))
    choice()
  elif b == "4":
    volume()
    clear()
    print("Volume: " + str(vol))
    choice()
  elif b == "5":
    main()
  elif b == "6":
    clear()
  else:
    main()

def circumference():
  global cir 
  cir = 2 * pi * a 
  
def area():
  global ar
  ar = pi * a ** 2 
  
def surfacearea():
  global surface 
  surface = 4 * pi * a ** 2

def volume():
  global vol 
  vol = 4/3 * pi * a ** 3

def error():
  print("Error!!!")
  main()
    
main()
