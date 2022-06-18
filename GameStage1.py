import os
import time

print("You open your eyes.")
time.sleep(2)
print("This isn't where you were a second ago.")
time.sleep(2)
print("You're lying on a cold, hard, tiled floor. It is pitch black.")
time.sleep(2)
print("You stand up and feel around. You feel hard walls behind and on either side of you. But you feel nothing in front of you.")
time.sleep(2)
print("You decide that you are in a hallway of sorts. You try to decide what to do next.")
time.sleep(2)


def level0(key):
  choice1 = input("What do you want to do: (1) Check the walls for a light (2) Walk forward blindly (3) Scream for help? Choice: ")

  while choice1 != "2":
    if choice1 == "1":
      print("You feel around on the walls carefully for a light switch. However, you can't find anything; the walls are perfectly smooth.")
      time.sleep(2)
      level0(key)
    
    if choice1 == "3":
      print("You scream 'HELP' at the top of your lungs, but in response hear only your frightened cry echo back to you. You are completely alone.")
      time.sleep(2)
      level0(key)

    else:
      print("That's not a valid option.")
      level0(key)

  if choice1 == "2":
    print("You carefully stretch your arms out and take a tentative step forward. Feeling nothing in front of you, you keep walking. Eventually you feel something in front of you -- another wall.")
    time.sleep(3)
    print("You feel around this wall too. Your hand hits something protruding outwards. A handle.")
    time.sleep(3)
    print("You open the door in front of you and step through.")
    time.sleep(3)
    os.system('clear')
    
    print("You step into a dimly lit circular room. There are three doors in front of you -- one slightly to the right, one directly in front of you, and one slightly to the left. The door you have just stepped throught slams shut behind you.")
    time.sleep(3)
  return key


def level1(key):
  choice2 = input("Which door do you want to approach: (0) The door behind you (1) The right door (2) The center door (3) The left door? Choice: ")
  
  while choice2 not in ["0", "1", "2", "3"]:
    print("That's not a valid option.")
    level1(key)
  
  if choice2 == "0":
    os.system('clear')
    print("You step back through the original door and somehow find yourself standing back in the pitch black hallway that you had just exited. You try to decide what to do next.")
    level0(key)
    level1(key)
  if choice2 == "2":
    os.system('clear')
    print("You open the middle door and are greeted by a harsh light.")
    time.sleep(2)
    print("As your eyes adjust to the brightness, you can make out a cracked stone floor. And in the center of the room, a bathtub sized crater.")
    time.sleep(2)    
    print("The crater is filled with molten metal, steaming and crackling and illuminating your surroundings.")
    time.sleep(2)
    print("As you take in the shocking sight ahead of you, you try to decide what to do.")
    time.sleep(2)
    
    choice2b = input("What do you want to do: (1) Step closer to the molten metal to investigate (2) Go back into the circular room through the door you just came in from? Choice: ")
    
    while choice2b not in ["1", "2"]:
      print("That's not a valid option.")
      choice2b = input("What do you want to do: (1) Step closer to the molten metal to investigate (2) Go back into the circular room through the door you just came in from? Choice: ")
      
    if choice2b == "1":
      print("You step up to the crater full of molten metal. As you do, cracks spread around you in the floor, but you do not notice. As you take a final step, the thin concrete floor breaks beneath you and you are dumped into the molten metal. You die in agony.")
      time.sleep(7)
      os.system('clear')
      time.sleep(1)
      print("Game over.")
      quit()

    if choice2b == "2":
      os.system('clear')
      print("You step back into the center of the circular room. There are three doors in front of you -- one slightly to the right, one directly in front of you (that you had just came through), and one slightly to the left. The door behind you leads to the dark hallway.")
      time.sleep(2)
      level1(key)
    
  if choice2 == "3":
    os.system('clear')
    print("You step through the left door. It is pitch black in this room, but some of the light from the circular room spills in. As your eyes adjust, you realize that the room is empty. You try to decide what to do next.")
    time.sleep(3)
  
    choice2c = input("What do you want to do: (1) Try to search this room carefully (2) Go back into the circular room through the door you just came in from? Choice: ")

    while choice2c not in ["1", "2"]:
      print("That's not a valid option.")
      choice2c = input("What do you want to do: (1) Try to search this room carefully (2) Go back into the circular room through the door you just came in from? Choice: ")
      
    if choice2c == "1":
      print("You wait and carefully search the room -- without moving, you peer at every space you see, and after you determine that it is safe, you tentatively move around and search the room more thorougly.")
      time.sleep(2)
      print("You are almost ready to give up, when you spot a tiny key lying in a far corner.")
      time.sleep(2)
      
      choice2c1 = input("Do you want to pick up this key (1) Yes (2) No? Choice: ")
      
      while choice2c1 not in ["1", "2"]:
        print("That's not a valid option.")
        choice2c1 = input("Do you want to pick up this key (1) Yes (2) No? Choice: ")
        
      if choice2c1 == "1":
        key = True
        print("You have picked up the key.")
        time.sleep(2)
        os.system('clear')
        print("You leave this room and step back into the center of the circular room. There are three doors in front of you -- one slightly to the right, one directly in front of you, and one slightly to the left (that you had just came through). The door behind you leads to the dark hallway.")
        time.sleep(2)
        level1(True)
        
      if choice2c1 == "2":
        print("You do not pick up the key.")
        time.sleep(2)
        os.system('clear')
        print("You leave this room and step back into the center of the circular room. There are three doors in front of you -- one slightly to the right, one directly in front of you, and one slightly to the left (that you had just came through). The door behind you leads to the dark hallway.")
        time.sleep(2)
        level1(key)
    
    if choice2c == "2":
      os.system('clear')
      print("You step back into the center of the circular room. There are three doors in front of you -- one slightly to the right, one directly in front of you, and one slightly to the left (that you had just came through). The door behind you leads to the dark hallway.")
      time.sleep(2)
      level1(key)

  if choice2 == "1":
    os.system('clear')
    print("You step up to the right door. When you try to turn the handle, it doesn't move -- the door is locked. As you examine it slightly closer, you notice that the door handle has something new on it: a keyhole, that can only be opened with a tiny key.")
    time.sleep(3)
    
    if key == True:
      print("You take out the key that you found in the leftmost room. You try to fit it into the lock, and it slides in perfectly. You turn the key and try the handle once more, this time the door opens. You step through door.")
      time.sleep(5)
      
    if key == False:
      print("You step away from the door and back into the middle of the circular room. There are three doors in front of you -- one slightly to the right (that you had just stepped away from), one directly in front of you, and one slightly to the left. The door behind you leads to the dark hallway.")
      time.sleep(3)
      level1(key)
transition = level0(False)
level1(transition)