#Basically allows you to use some cool functions.
import time 
import replit

#Defining a function. The parenthesis is necessary btw. def means define, then followed by 
#the function's name AKA start()
def start():
  #print() allows you to print a string, you need the quotations tho!!!
  #If you want to print a variable, put the variable name in the parenthesis with no quotations!
  #The line replit.clear() clears the screen.
  replit.clear()
  print("Bob Has No Girlfriend")
  print("=====================")
  print("By Caleb Turner")
  #time.sleep() allows you to basically tell the code to wait a certain amount of time, in seconds(which
  #goes in the parenthesis), before moving on to the next line(s) of code.
  time.sleep(5)
  #This calls the function "intro()", which them makes the computer run all the code contained in that function.
  intro()
  
#Now we define the function "intro()" and all the code that it contains
def intro():
  #The line replit.clear() clears the screen.
  replit.clear()
  #The line of code "\n" is used to break a line. Basically, it makes your text skip to line below it's current
  #location.
  print("Bob plays and loves Minecraft.\nBecause of this, Bob has no girlfriend.")
  time.sleep(4)
  #You ask for user input. I named whatever the input is "op1", for option one.
  op1 = input("\nSad, ain't it?")
  #You check to see if the input you were given is "yeah". In python you use double equals signs for things
  #like this.
  if op1 == "yes":
    #What is does
    print("\nPoor Bob..")
    time.sleep(3)
    #After three seconds you call for the function "end()"
    end()
    
  #"elif" means "else if", just shortened. If your statement doesn't equal "yeah", you check
  #if it equals "not really", if it does, you run this code.
  elif op1 == "no":
    #What it do
    print("\nYou heartless monster!")
    time.sleep(3)
    #After three seconds you call for the function "end()"
    end()
    
#Defining the function "end()". Basically, the end of the game.
def end():
  replit.clear()
  print("Game over!!")
  time.sleep(3)
  #call for the function "restart()"
  restart()
  
#Defining "restart()"
def restart():
  rs = input("Play Again?")
  
  if rs == "yes":
    time.sleep(1)
    print("\nHave Fun!!")
    time.sleep(3)
    #Go back to the starting fuction(the beginning of the game)
    start()
    
  #if they don't want to restart the game, it says goodbye and clears the screen.
  elif rs == "no":
    time.sleep(1)
    print("\nGoodbye!!")
    time.sleep(3)
    replit.clear()
    
start()
