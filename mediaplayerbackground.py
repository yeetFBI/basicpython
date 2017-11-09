#Meant to be used in repl.it
import time 
import random
import replit
import sys 

#Variables
playlists = []
allsongs = ["Billy Jean", "Circles", "XO"]
shuffle = False
pause = False
start = 0
global playS
playS = False
global playP
playP = False

def clear():
  replit.clear()
  
def wait(float):
  time.sleep(float)
  
#Actual Code n Crap
def init():
  clear()
  print("__   __        _  ______ _                       ")
  print("\ \ / /       | | | ___ \ |                      ")
  print(" \ V /___  ___| |_| |_/ / | __ _ _   _  ___ _ __ ")
  print("  \ // _ \/ _ \ __|  __/| |/ _` | | | |/ _ \ '__|")
  print("  | |  __/  __/ |_| |   | | (_| | |_| |  __/ |   ")
  print("  \_/\___|\___|\__\_|   |_|\__,_|\__, |\___|_|   ")
  print("                                  __/ |          ")
  print("                                 |___/           ")
  wait(5)
  choice1()
  
#Asks the user what they would like to do
def choice1():
  clear()
  print("[1]Edit a Playlist, [2]Play a Song, [3]Play a Playlist, or [4]End the Program?")
  desire = input("")
  if desire == "1":
    playlistEdit()
  elif desire == "2":
    playSong()
  elif desire == "3":
    playPlaylist()
  elif desire == "4":
    clear()
    sys.exit()
  else:
    choice1()
    
#Asks the user whether they want to create or add to a playlist
def playlistEdit():
  clear()
  print("[1]Create, [2]Add to a Playlist, or [3]Remove Songs from a playlist?")
  edit = input("")
  if edit == "1":
    createPlaylist()
  elif edit == "2":
    addPlaylist()
  elif edit == "3":
    removePlaylist()
  elif edit == "back":
    choice1()
  else:
    playlistEdit()
    
#They create a new playlist(list) with a user assigned name
def createPlaylist():
  clear()
  in1 = input("Name of Playlist?")
  #Adds the playlist name to our list of playlist names
  playlists.append(in1)
  global a
  #Creates the list under the global variable of a
  a = vars()[in1] = []
  clear()
  print("Adding songs to " + in1 + "(Type done when finished):")
  while True:
    in2 = input("\n")
    if in2 != "" and in2 != "done":
      a.append(in2)
      allsongs.append(in2)
    elif in2 == "done":
      #print(len(a))
      choice1()
      
#Add to Playlist 
def addPlaylist():
  clear()
  print("PLAYLISTS")
  print("------------------")
  print('\n'.join(playlists))
  print("------------------")
  i1 = input("Which Playlist?")
  clear()
  print("Adding songs to " + i1 + "(Type done when finished):")
  while True:
    i2 = input("\n")
    if i2 != "" and i2 != "done":
      a.append(i2)
      allsongs.append(i2)
    elif i2 == "done":
      choice1()

#Remove songs from a playlist
def removePlaylist():
  clear()
  print("PLAYLISTS")
  print("------------------")
  print('\n'.join(playlists))
  print("------------------")
  i1 = input("Which Playlist?")
  if i1 in playlists:
    clear()
    print("Songs")
    print("------------------")
    print('\n'.join(a))
    print("------------------")
    print("Removing songs from " + i1 + "(Type done when finished):")
    while True:
      i2 = input("\n")
      if i2 != "" and i2 != "done":
        a.remove(i2)
        allsongs.remove(i2)
      elif i2 == "done":
        choice1()
  else:
    print("There isn't a playlist like that!")
    choice1()
      
#Play a Songs
def playSong():
  global shuffle
  shuffle = False
  clear()
  print("Your Songs:\n-------------")
  for index, item in enumerate(allsongs):
    print(str(index + 1) + ": " + str(item))
  print("-------------\n")
  print("Which Song to Play?")
  global song
  song = input("\n")
  playingSong()
    
def playingSong():
  clear()
  if song in allsongs:
    sTrue()
    print("Now playing " + song + "...")
    print("[1]Pause/Play, [2]Stop, [3]Shuffle,  [4]Skip, [5]Previous, or [6] Search for Song")
    songOptions = input("")
    
    if songOptions == "1":
      pauseHandler()
    elif songOptions == "2":
      sFalse()
      choice1()
    elif songOptions == "3":
      shuffleHandler()
    elif songOptions == "4":
      skipper()
    elif songOptions == "5":
      previous()
    elif songOptions == "6":
      playSong()
    else:
      playSong()
      
  else:
    print("You don't have that song stored!!\n")
    playSong()
    
def playPlaylist():
  clear()
  print("Your Playlists:\n-------------")
  for index, item in enumerate(playlists):
    print(str(index + 1) + ": " + str(item))
  print("-------------\n")
  print("Which Playlist to Play?")
  global wp 
  wp = input("\n")
  playingPlaylist()
  

def playingPlaylist():
  clear()
  if wp in playlists:
    global song 
    song = a[0]
    playing()
  else:
    print("Error!")
    choice1()
    
#Tells you what is currently playing and gives you your choices
def playing():
  pTrue()
  clear()
  print("Now playing " + song + "...")
  print("[1]Pause/Play, [2]Stop, [3]Shuffle,  [4]Skip, [5]Previous, or [6] Search for Song")
  songOptions = input("")
    
  if songOptions == "1":
    pauseHandler()
  elif songOptions == "2":
    pFalse()
    choice1()
  elif songOptions == "3":
    shuffleHandler()
  elif songOptions == "4":
    skipper()
  elif songOptions == "5":
    previous()
  elif songOptions == "6":
    playSong()
  else:
    playSong()
        
  
    
#Welcome to the hell hole

def previous():
  if playS == True:
    recallSong()
    playingSong()
  elif playP == True:
    recallSong()
    playing()

def shuffleHandler():
  if shuffle == True:
    if playS == True:
      shuffFalse()
      playingSong()
    elif playP == True:
      shuffFalse()
      playing()
  elif shuffle == False:
    if playS == True:
      shuffTrue()
      playingSong()
    elif playP == True:
      shuffTrue()
      playing()

def skipper():
  saveSong()
  if shuffle == True:
    if playS == True:
      setsongA()
      playingSong()
    elif playP == True:
      setsongB()
      playing()
      
  elif shuffle == False:
    addIndex()
    if playS == True:
      if start <= int(len(allsongs) - 1):
        setsong1()
        playingSong()
      elif start > int(len(allsongs) - 1):
        rsS()
        playingSong()
    elif playP == True:
      if start <= int(len(a) - 1):
        setsong2()
        playing()
      elif start > int(len(a) - 1):
        rsP()
        playing()
        
def pauseHandler():
  if playS == True:
    if pause == False:
      pauseTrue()
      while pause == True:
        clear()
        print("Paused... Type 1 to Play Again..")
        p1 = input("\n")
        if p1 == "1":
          pauseFalse()
          break
      playingSong()
  elif playP == True:
    if pause == False:
      pauseTrue()
      while pause == True:
        clear()
        print("Paused... Type 1 to Play Again..")
        p2 = input("\n")
        if p2 == "1":
          pauseFalse()
          break
    playing()

def saveSong():
  global saved 
  saved = song 
  
def recallSong():
  global song 
  song = saved

def setsongA():
  r = random.choice(allsongs)
  global song 
  song = r
  
def setsongB():
  r = random.choice(a)
  global song 
  song = r
      
def setsong1():
  global song 
  song = allsongs[start]
  
def setsong2():
  global song 
  song = a[start]

def addIndex():
  if playS == True:
    startS()
  elif playP == True:
    startP()
    
def rsS():
  global song 
  song = allsongs[0]
  
def rsP():
  global song 
  song = a[0]
    
def startS():
  global start
  start = allsongs.index(str(song))
  addStart()
  
def startP():
  global start
  start = a.index(str(song))
  addStart()
  
def addStart():
  global start
  start = start + 1

def sTrue():
  global playS
  playS = True 
  
def sFalse():
  global playS
  playS = False 
  
def pTrue():
  global playP 
  playP = True 
  
def pFalse():
  global playP 
  playP = False
  
def pauseTrue():
  if playS == True:
    global pause 
    pause = True 
  
def pauseFalse():
  global pause 
  pause = False 
  
def shuffTrue():
  global shuffle 
  shuffle = True 
  
def shuffFalse():
  global shuffle 
  shuffle = False
  
  
init()
#choice1()
