#Pi Project
#By Caleb Turner and Jaxon McKinlay
#Description:
#It basically asks for input and then allows the user to get circumference, area, surface area, or volume of the object. Loops until the user inputs "6", or done.
from math import pi 
import replit
import time 

multVar = pi 

def clear():
  replit.clear()

def wait(float):
  time.sleep(float)

#Introduction. Prints our title and our names
def init():
  clear()
  print("   ____    _    ____    ___     __")
  wait(.5)
  print("  / ___|  / \  / ___|  / \ \   / /")
  wait(.5)
  print(" | |     / _ \ \___ \ / _ \ \ / / ")
  wait(.5)
  print(" | |___ / ___ \ ___) / ___ \ V /  ")
  wait(.5)
  print("  \____/_/   \_\____/_/   \_\_/   ")
  wait(.5)
  print("(Circumference, Area, Surface Area, and Volume)")
  print(" By Caleb Turner and Jaxon McKinlay")
  wait(2)
  main()
  
def main():
  clear()
  global a 
  #Ask for the radius of the circle or sphere. Needs to be a number.
  a = float(input("Radius of Circle or Sphere(Needs to be a Number!!): "))
  if a != "":
    clear()
    choice1()
  elif a == "":
    error()
    
def choice1():
  #Prints the options of what to calculate
  print("Radius: " + str(a))
  print("Would you like to find: \n[1]Circumference(Circle)\n[2]Area(Circle)\n[3]Surface Area(Sphere)\n[4]Volume(Sphere)\n[5]Enter a New Radius\n[6]Done")
  b = input("")
  if b == "1":
    #Will take the user to the circumference function
    circumference()
    clear()
    #Prints the circumference
    print("Circumference: " + str(cir) + "\n-----------------")
    #Goes back to the start of choice1
    choice1()
  elif b == "2":
    #Takes the user to the area function
    area()
    clear()
    #Prints the area
    print("Area: " + str(ar) + "\n-----------------")
    #Goes back to the start of choice1
    choice1()
  elif b == "3":
    #Takes the user to surface area function
    surfacearea() 
    clear()
    #Prints surface area
    print("Surface Area: " + str(surface) + "\n-----------------")
    #Goes back to the start of choice1
    choice1()
  elif b == "4":
    #Takes the user to the volume function
    volume()
    clear()
    #Prints the volume
    print("Volume: " + str(vol) + "\n-----------------")
    #Goes back to the start of choice1
    choice1()
  elif b == "5":
    main()
  elif b == "6":
    clear()
  else:
    main()

def circumference():
  global cir 
  #Sets a variable to the equation for circumference(2*pi*r)
  cir = 2 * multVar * a 
  
def area():
  global ar
  #Sets a variable to the equation for area(pi*r^2)
  ar = multVar * a ** 2 
  
def surfacearea():
  global surface 
  #Sets a variable to the equation for surface area
  surface = 4 * multVar * a ** 2

def volume():
  global vol 
  #Sets a variable to the equation for volume
  vol = (4/3) * multVar * a ** 3

def error():
  print("Error!!!")
  main()
    
init()
