# originally in Replit
# https://replit.com/@anushaveluri/GROUPPROJECT?from=notifications#main.py

import random
import time

# movement and ID system
class Room():
  def __init__(self):
    self.room_numL = 9
    self.room_numR = 0
    self.room_numF = 0
    self.roomNum = 900
    self.room_Name = "House Txts/house room 900.txt"
  def current(self):
    self.roomNum = str(self.room_numL) + str(self.room_numR) + str(self.room_numF)
    return self.room_Name

  # to move right, either increase x00 or decrease 0x0
  def moveR(self):
    if self.room_numR >= 0:
      if self.room_numL == 9:
        self.room_numR += 1
      elif self.room_numL == 1:
        self.room_numL = 9
      elif self.room_numL != 9 or self.room_numL != 1:
        self.room_numL -= 1
      self.room_Name = "House Txts/house room " + str(self.room_numL) + str(self.room_numR) + str(self.room_numF) + ".txt"
    else:
      print("You cannot do that.")

  # to move left, either increase 0x0 or decrease x00
  def moveL(self):
    if self.room_numL > 0:
      if self.room_numL == 9 and self.room_numR == 0:
        self.room_numL = 1
      elif self.room_numL == 9 and self.room_numR != 0:
        self.room_numR -= 1
      elif self.room_numL != 9 and self.room_numR == 0:
        self.room_numL += 1
      self.room_Name = "House Txts/house room " + str(self.room_numL) + str(self.room_numR) + str(self.room_numF) + ".txt"
    else:
      print("You cannot do that.")

  # to move back, decrease 00x
  def moveB(self):
    if self.room_numF >= 0:
      self.room_numF -= 1
      self.room_Name = "House Txts/house room " + str(self.room_numL) + str(self.room_numR) + str(self.room_numF) + ".txt"
    else:
        print("You cannot do that.")

  # to move forward, increase 00x
  def moveF(self):
    self.room_numF += 1
    self.room_Name = "House Txts/house room " + str(self.room_numL) + str(self.room_numR) + str(self.room_numF) + ".txt"

# auto-quits
def death_Message():
  print("You have died! Try again next time.")
  quit()

# important player things
class Player():
    def __init__(self, name_input):
        self.alive = True
        self.has_won = False
        # this is the default health points
        self.health = 12
        # default added health gained
        self.additional_health = 0
        # how much damage character does by default
        self.attack_power = random.randint(4, 6)
        # name
        self.name = name_input
        # default shards
        self.item_shard = 0
        self.room = "begin room 1.txt"

        self.letter_have = False

        self.health_items = 0

        # room triggers
        self.found900 = False
        self.found101 = False
        self.found902 = False
        self.found922 = False
        self.found104 = False
        self.found914 = False
    
    # player can call in an encounter
    def attack(self):
      dam = random.randint(4, 6)
      print("You attacked, and did " + str(dam) + " damage.")
      return dam

    # player can call whenever
    def inventory_check(self):
      if self.letter_have:
        print("You have " + str(self.health_items) + " health item(s), " + str(self.item_shard) + " key item(s), and an old letter.")
      else:
        print("You have " + str(self.health_items) + " health item(s) and " + str(self.item_shard) + " key item(s).")

    def health_refresh(self):
        self.health = 12
        self.health += self.additional_health

    def health_add(self):
        self.additional_health += 4
        self.health += 4
        self.health_items += 1

    # player can call whenever
    def health_check(self):
        print(
            str(self.health) + " HP/" + str(12 + self.additional_health) +
            " HP")

    def check_room(self):
        # analyze what's interesting in the room, reading text file
        self.room = house.room_Name
        f = open(self.room)
        line = f.readline()
        while (line):
            print(line)
            line = f.readline()

    def item_add(self):
      if self.item_shard < 6:
        self.item_shard += 1
    def letter(self):
      if self.letter:
        print("# If you're reading this, it's too late to turn back. I couldn't escape but maybe you can. I tried to solve these riddles but... I couldn't survive the monsters...")
        print("# Riddle 1: in a place where the path is unclear and turns twisting, solve the puzzle to find your desired prize while persisting.")
        print("# Riddle 2: where the master sleeps, fight the guardian to receive the item he keeps.")
        print("# Riddle 3: in the room in which things are brought to life, fight the maiden who brings all manners of strife.")
        print("# Riddle 4: the room that preserves all grains of rice, solve the puzzle to receive the prize that cannot be found twice.")
        print("# Riddle 5: the room in which to flee from, defeat the master and escape with a 5 sum.")


name_input = input("What is your name? ")
name_input = Player(name_input)

class Guardian():
  def __init__(self):
    self.health = 16
    self.attackdam = random.randint(2, 6)
  def attack(self):
    damage = random.randint(2, 6)
    name_input.health -= damage
    print("The Guardian attacked and did " + str(damage) + " damage.")
    print("You have " + str(name_input.health) + " HP left.")
    if (name_input.health <= 0):
      death_Message()
  def death(self):
    if self.health <= 0:
      print("The Guardian has died!")

class Maiden():
  def __init__(self):
    self.health = 6
    self.attackdam = random.randint(8, 12)
  def attack(self):
    damage = random.randint(8, 12)
    name_input.health -= damage
    print("The Maiden attacked and did " + str(damage) + " damage.")
    print("You have " + str(name_input.health) + " HP left.")
    if (name_input.health <= 0):
      death_Message()
  def death(self):
    if self.health <= 0:
      print("The Maiden has died!")

class Master():
  def __init__(self):
    self.health = 16
    self.attackdam = random.randint(4, 12)
  def attack(self):
    damage = random.randint(4, 12)
    name_input.health -= damage
    print("The Master attacked and did " + str(damage) + " damage.")
    print("You have " + str(name_input.health) + " HP left.")
    if (name_input.health <= 0):
      death_Message()
  def death(self):
    if self.health <= 0:
      print("The Master has died!")

guard = Guardian()
maid = Maiden()
mast = Master()

def room_921_riddle():
  print("There are two stone lions. One always lies, the other always tells the truth. Ahead of you are two boxes. When you ask the lion to the right which box the other lion will choose, he points to the box to your left. When you ask the lion to the left which box the other lion will choose, he points to the left.")
  choice = input("Which box do you choose? (L/R): ")
  if choice == "L":
    death_Message()
  elif choice == "R":
    name_input.success = True

def room_202_puzzle():
  print("You find a series of numbers etched into the wall:")
  print("37, 10, 82")
  print("29, 11, 47")
  print("96, 15, 87")
  print("42, ?, 15")
  choice = input("What is the missing number?: ")
  if choice == "6":
    name_input.success = True
  else:
    death_Message()

# house room event triggers
def room_103_fight():
  print("The Guardian of the Master has appeared and has challenged you!")
  while(guard.health > 0 and name_input.health > 0):
    guard.attack()
    action = input("What will you do? (attack): ")
    if action == "attack":
      guard.health -= name_input.attack()
      print("The Guardian has " + str(guard.health) + " HP left.")
    else:
      print("You cannot do that.")
  if guard.health <= 0:
    name_input.success = True
    guard.death()
  elif name_input.health <= 0:
    death_Message()
    
def room_922_fight():
  print("The Maiden of the mansion, long to time, has attacked you!")
  while(maid.health > 0 and name_input.health > 0):
    maid.attack()
    action = input("What will you do? (attack): ")
    if action == "attack":
      maid.health -= name_input.attack()
      print("The Maiden has " + str(maid.health) + " HP left.")
    else:
      print("You cannot do that.")
  if maid.health <= 0:
    name_input.success = True
    maid.death()
  elif name_input.health <= 0:
    death_Message()

def room_934_fight():
  print("The Master has appeared and has challenged you!")
  while(mast.health > 0 and name_input.health >0):
    mast.attack()
    action = input("What will you do? (attack): ")
    if action == "attack":
      mast.health -= name_input.attack()
      print("The Master has " + str(mast.health) + " HP left.")
    else:
      print("You cannot do that.")
    if mast.health <= 0:
      name_input.success = True
      mast.death()
    elif name_input.health <= 0:
      death_Message()
      
def room_900_event():
  print("# The forested area provides shade from the blinding sun. A path seems to have been well-worn into the ground, as if many people or animals have taken this path before. It seems like the right path, though you wonder briefly why it seems that you can't go back.")
  print("# The structure begins to take shape as you approach, the foliage thinning out, and then opening up to reveal a broken down house. House is perhaps a light word, it's more of a mansion with spanning rooms, and clearly old in terms of architectural design. The outside of the house is overgrown and smells of mold.")
  print("# You find a worn piece of paper on the ground. It says the following:")
  name_input.letter()
  name_input.letter_have = True
  room_dict.pop(900)
def room_100_event():
  print("# The gate ominously creaks on its hinges, yet the path leading to it is worn enough that you can see footprints in the dirt. Strange, the house looks abandoned.")
  room_dict.pop(100)
def room_910_event():
  print("# The pond has a shallow pool of water in the bottom. Mosquitoes buzz irritatingly in your ear.")
  room_dict.pop(910)
def room_901_event():
  print("# The room is grand, despite the peeling wallpaper, torn-up carpet, and busted windows. Said broken windows let enough light filter in that you can see clearly, despite the absence of working electricity.")
  room_dict.pop(901)
def room_101_event():
  print("# Weeds have flourished in the boxes which might've once held fruit and vegetables. Long grasses and invasive plants with spiked leaves nearly completely cover what might be a path.")
  room_dict.pop(101)
def room_911_event():
  print("# The stones of the structure are mossy and worn down with age, but the shade provided is still welcome. Perhaps at an earlier period, it would've served as a lovely meeting spot.")
  room_dict.pop(911)
def room_921_event():
  print("# The labyrinth's entrance is blocked off by fallen rocks, not like the maze is very appealing in the first place. However, two stone lions at the maze's entrance catch your attention.")
  name_input.success = False
  room_921_riddle()
  if (name_input.success):
    print("The honest lion to the left says: 'Congratulations, you have solved the riddle. Take your prize.'")
    name_input.item_add()
    room_dict.pop(921)
  else:
    pass
def room_202_event():
  print("# The storage room is very dark and smells strongly of expired goods. Despite this, and with the fading light from the entryway, you persist.")
  name_input.success = False
  room_202_puzzle()
  if (name_input.success == True):
    print("The wall opens up to reveal the shard of a key. You take it.")
    name_input.item_add()
    room_dict.pop(202)
def room_102_event():
  # this room will always reset health
  print("# For an old house, the kitchen is remarkably homey, perhaps the most comfort you've felt since waking up.")
  print("This place fills you with strength. You feel refreshed.")
  name_input.health_refresh()
def room_902_event():
  print("# The long dining table is broken in several places. Curtains that might've once held back the natural light are moth-eaten, and illuminate the wear and tear in a room which might've once been magnificent.")
  room_dict.pop(902)
def room_922_event():
  print("# The crafting room is small and cramped by comparison to the other rooms you've visited. You don't get much time before you realize you're not alone.")
  name_input.success = False
  room_922_fight()
  if name_input.success:
    print("Congratulations, you have won your prize.")
    name_input.item_add()
    room_dict.pop(922)
def room_203_event():
  print("# The fresh air welcomes you. Despite the broken fragments of stone, the balcony is a welcome reminder of the outside world.")
  room_dict.pop(203)
def room_103_event():
  print("The bed, or what might've been a bed, is broken to the point of no repair. The frame is shattered, linens torn apart, and whatever other pieces of furniture that might've populated the room are piles of debrise. It doesn't take long for you to realize you aren't alone, and you barely have time to react when the Guardian attacks.")
  name_input.success = False
  room_103_fight()
  if (name_input.success == True):
    print("Congratulations, you have won your prize.")
    name_input.item_add()
    room_dict.pop(103)
def room_104_event():
  print("# Spacious for a closet, though nothing catches your eye. Nevermind that the light doesn't reach far.")
  room_dict.pop(104)
def room_903_event():
  print("# The hallway walls are made of fine wood that's been rotted from the inside out. Ew.")
  room_dict.pop(903)
def room_913_event():
  print("# This room is incredibly spacious, large windows let in natural light and cast eerie shadows over the smooth, unobstructed walls. If you listen closely, you can almost hear the sound of instruments and life.")
  room_dict.pop(913)
def room_923_event():
  print("# Smaller, but no less grand, is the music room. Traces of what might've been a grand piano linger in the indents on the floor, and old metal that might've held music sheets litter the room.")
  room_dict.pop(923)
def room_933_event():
  print("Very little natural light reaches this room, so you shuffle blindly through pieces of broken wood.")
  room_dict.pop(933)
def room_914_event():
  print("# You can imagine tired dancers retreating to this place of solitude for a breath of fresh air. You breathe in deeply.")
  room_dict.pop(914)
def room_924_event():
  print("# The space is cramped and dark.")
  room_dict.pop(924)
def room_934_event():
  print("# You are immediately confronted with an apparition who does not seem friendly.")
  name_input.success = False
  room_934_fight()
  if (name_input.success == True):
    print("Congratulations, you have won your prize.")
    name_input.item_add()
    room_dict.pop(934)
def room_944_event():
  print("# Blessedly, the outside welcomes you. A door that seemingly leads nowhere catches your attention.")
  if name_input.item_shard == 5:
    win = True
    if win:
      print("# With the 5 key shards you found, you piece them together and slip the key into the door. The door clicks open.")
      print("Congratulations, you have won the game!")
      print("Thank you for playing!")
      quit()
  else:
    pass

room_id = []
# house room ID list is they've already visited

room_dict = {900:room_900_event, 100:room_100_event, 910:room_910_event, 901:room_901_event, 101:room_101_event, 911:room_911_event, 921:room_921_event, 202:room_202_event, 102:room_102_event, 902:room_902_event, 922:room_922_event, 203:room_203_event, 103:room_103_event, 104:room_104_event, 903:room_903_event, 913:room_913_event, 923:room_923_event, 933:room_933_event, 914:room_914_event, 924:room_924_event, 934:room_934_event, 944:room_944_event}

def actions_house():
  # flags for looking for options
  r_option = False
  l_option = False
  f_option = False
  b_option = False
  found = False
  health = False
  
  file = house.current()
  f = open(file)
  line = f.readline()
  id = line
  for i in range(len(room_id)):
    if id == room_id[i]:
      found = True
  if found == False:
    room_id.append(id)
    room_dict[int(house.roomNum)]()
  while(line):
    print(line)
    line = f.readline()

  if house.roomNum == "102":
    room_102_event()

  if house.roomNum == "944":
    room_944_event()

  g = open(file)
  gline = g.readline()
  while(gline):
    if "right" in gline:
      r_option = True
    if "left" in gline:
      l_option = True
    if "Ahead" in gline:
      f_option = True
    if "Behind" in gline:
      b_option = True
    if "health" in gline:
      health = True
    gline = g.readline()
  
  choice = True
  
  while (choice):
        # input options to do things while "alive" that will only go false if you die or quit
    status = input("What do you want to do next?: ")
    if status == "quit":
      exit()
    elif status == "help":
            # basic commands
      print("'check inv' will check your key items and other pick ups")
      print("'check health' will check your current health points (HP)")
      print("'check room' will analyze the current room for options'")
      print("'pick up' lets you pick up an interesting item")
      print("'read letter' lets you reread the letter you found on the ground in the courtyard")
      print("")
      print("'go left' 'go right' 'go foward' 'go back' are movement commands that will place you in a different setting")
      print("'quit' will completely stop the program")

    elif status == "check inv":
      name_input.inventory_check()
    elif status == "check health":
      name_input.health_check()
    elif status == "check room":
      name_input.check_room()
    elif status == "read letter":
      name_input.letter()
    elif status == "go back":
      if b_option:
        house.moveB()
        actions_house()
      else:
        print("You cannot go back.")
    elif status == "go forward":
      if f_option:
        house.moveF()
        actions_house()
      else:
        print("You cannot go forward.")
    elif status == "go left":
      if l_option:
        house.moveL()
        actions_house()
      else:
        print("You cannot go left.")
    elif status == "go right":
      if r_option:
        house.moveR()
        actions_house()
      else:
        print("You cannot go right.")
    elif status == "pick up":
      if (health):
        if (house.roomNum == "900" and name_input.found900 == False):
          print("You have found a very healthy petal. You feel stronger.")
          name_input.found900 = True
          name_input.health_add()
        elif (house.roomNum == "101" and name_input.found101 == False):
          print("You have found a very healthy fruit. You feel stronger.")
          name_input.found101 = True
          name_input.health_add()
        elif (house.roomNum == "902" and name_input.found902 == False):
          print("You have found a very healthy drink. You feel stronger.")
          name_input.found902 = True
          name_input.health_add()
        elif (house.roomNum == "922" and name_input.found922 == False):
          print("You have found a very healthy paint brush. You feel stronger.")
          name_input.found922 = True
          name_input.health_add()
        elif (house.roomNum == "104" and name_input.found104 == False):
          print("You have found a very healthy pin. You feel stronger.")
          name_input.found104 = True
          name_input.health_add()
        elif (house.roomNum == "914" and name_input.found914 == False):
          print("You have found a very healthy flower. You feel stronger.")
          name_input.found914 = True
          name_input.health_add()
        else:
          print("You've already picked everything up.")
      else:
        print("There is nothing to pick up.")
    else:
      print("You can't do that.")

def actions_basic():
    # this will allow basic actions to be called at any point
    choice = True
    while (choice):
        # input options to do things while "alive" that will only go false if you die or quit

        status = input("What do you want to do next?: ")
        if status == "quit" or status == "stop":
            # just stops the game loop
            choice = False
        elif status == "help":
            # basic commands
            print("'attack' will initiate a combat encounter")
            print("'check inv' will check your gold and key items")
            print("'check health' will check your current health points (HP)")
            print("'check room' will analyze the current room for options'")
            print("")
            print("'go left' 'go right' 'go foward' 'go back' are movement commands that will place you in a different setting")

        elif status == "check inv":
            name_input.inventory_check()
        elif status == "check health":
            name_input.health_check()
        elif status == "check room":
          intro = "intro.txt"
          f = open(intro)
          intro_line = f.readline()
          while(intro_line):
            print(intro_line)
            intro_line = f.readline()
            
        # embedded is more methodsssss for the different paths
        elif status == "go left":
            name_input.room = "House Txts/house room 900.txt"
            if (name_input.room == "House Txts/house room 900.txt"):
              actions_house()
            choice = False
        elif status == "go forward": 
          name_input.room = "mountain room 1.txt"
          if (name_input.room == "mountain room 1.txt"):
            actions_mountain()
            choice = False
        elif status == "go right":
            name_input.room = "beach.txt"
            print("You left the current area and have entered a new place.")
            if (name_input.room == "beach.txt"):
              actions_beach()
            choice = False
        elif status == "go back":
            if name_input.room == "begin room 1.txt":
                print("You cannot go back.")
            else:
                name_input.room = "begin room 1.txt"
                print("You have returned to your starting point.")
        else:
            print("You can't do that.")

house = Room()
intro = "intro.txt"
f = open(intro)
intro_line = f.readline()

# plays intro text once
while (intro_line):
    print(intro_line)
    intro_line = f.readline()

# should only technically play once
actions_basic()
