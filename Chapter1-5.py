#David Ramirez
#11/23/2024

#Import time to create a more lively text
import time
import Inventory
import sys

#I need to define chapter one and print out the scenary from milestone 2
def chapter_one():
    print("Chapter 1: The Awakening")
    print("\"I awoke in a place of ruin... A factory... the largest factory in the world, Wainwright Factory, but no one’s around.\"")
    


    #Add a "Type yes to continue" because it should be evenly paced
    while True:
        continue_yes = input("Type 'yes' to continue: ").strip().lower()
        if continue_yes == 'yes':
            break

    #The code should refer to the flowcharts option lists
    print("") #This part is a spacer so that the new batch of info is more noticeable
    print("\"A dark hall of endless factory machines looms ahead, what should I do?.\"")

    options = ["Look for a flashlight","Examine the glowing objects from the assembly line","Proceed to a corridor"]
    #Show the set of choices
    #Choice 1 should be added to the inventory which will appear in chapter
    #Flashlight should be false as I don't have it 

    flashlight_obtained = False

    #I should be able to return back to option list from option 1

    while True:

        for index, str in enumerate(options):
            print(f"{index+1}.{str.capitalize()}")

        try:
            choice = int(input("Choose an action from the list: "))

            if choice ==1:
                if not flashlight_obtained:
                        print("You have obtain a flashlight that protects your sanity")
                        time.sleep(2) #time delay
                        print("\"I feel safe...but at the same time, unlighten areas seem to be staring at me...\"")
                        print("")
                        flashlight_obtained = True #Flashlight is set true after clicking choice
                        Inventory.add_item("Flashlight")
                        time.sleep(2)
                        continue
                else:
                    print("I have a flashlight already")
                    continue
            elif choice ==2:
                    Touch = input(("Should I touch the object? ")).strip().lower()
                    if Touch == 'yes':
                        print("Examine the glowing objects from the assembly line")
                        time.sleep(2) #time delay
                        print("\"I feel like I've seen this before..\"")
                        time.sleep(2)
                        print("\"Something isn't right...This..crystal..\"")
                        time.sleep(3)
                        print("Unknown crackling sounds from the darken abyss race towards to the player (Dane Miller), as they get closer, the players life is taken")
                        time.sleep(6) #longer time for readablity
                        print("The end")
                        time.sleep(3)
                        Inventory.reset_inventory()
                        time.sleep(3)
                        chapter_one() #restart chapter
                    elif Touch =='no':
                        print("\"I'll just leave it\"")
                        continue
            elif choice ==3:
                print("You proceed to a corridor")
                time.sleep(2)
                print("Moving to chapter 2")
                time.sleep(2)
                chapter_two()
                return
            else:
                print("Choose a number from the list: ")
        
        except ValueError:
            print("Choose a number from the list 1-3")

def chapter_two():
    #All chapters should be similar, as it's a story driven game with some endings of those options
    #Inventory should be present including the rest of the chapters except chapter 1
    print("")#Adding space between the lines of text when transitioning
    print("Chapter 2: Corridor")
    print("\"I feel like I’ve been here before, an endless series of rooms where workers would get lost..\"")

    while True:
            continue_yes = input("Type 'yes' to continue: ").strip().lower()
            if continue_yes == 'yes':
                break
    
    
    #Enter room 265 (If the player has a flashlight they may enter, if not; a shadowy figure appears within room 265 running towards the player thus restarting to chapter 1) 
    #Enter room 264 (finds tools for fixing certain machines)
    #Enter room 263 (an operating room for managing certain assembly rooms but requires power)  
    #Return to the assembly hall (chapter 1)
    #Move to the end of the corridor to reveal another series of rooms (move to chapter 3)
    #Set up an option list from chapter 2, including inventory 
    print("Many options here, what should I do?")
    options = [

    "Check inventory",
    "Enter room 265",
    "Enter room 264",
    "Enter room 263",
    "Return to the assembly hall (chapter 1)",
    "Move to the end of the corridor to reveal another series of rooms (move to chapter 3)"
    ]

    Gas_Mask_Obtained = False

    while True:
        
        for index, str in enumerate(options):
            print(f"{index+1}.{str.capitalize()}")

        try:
            choice = int(input("Choose an action from the list: "))
            if choice ==1:
                Inventory.show_inventory()# Show inventory
                continue
            elif choice ==2:
                # Enter room 265 (only if the player has the flashlight if not, monster appears)
                if "Flashlight" in Inventory.inventory: # Check if Flashlight is in inventory
                    print("")#spacer
                    print("You enter room 265. The room is dark, but you can see with your flashlight.")
                    print("")#spacer
                    # Continue with room 265 events
                    time.sleep(2)
                    if not Gas_Mask_Obtained:
                        print("You have obtain a Gas Mask for certain situations")
                        time.sleep(2) #time delay
                        print("\"A Gas mask? might prove useful\"")
                        Gas_Mask_Obtained= True #Gas mask is set true after clicking choice
                        Inventory.add_item("Gas Mask")
                        print("")#spacer
                        time.sleep(2)
                    else:
                        print("")
                        print("Same place nothing new now")
                        print("")
                    continue
                else:
                    print("A shadowy figure appears in room 265 as you try to enter.")
                    time.sleep(3)
                    print("Crackling sounds emerge around you")
                    time.sleep(3)
                    print("YOU CANT ESCAPE")
                    time.sleep(2)
                    print("The creature stands up, it's height is double of your height..It speaks")
                    time.sleep(2)
                    print("y̯̣̼_̢̡̨̞̘̟̼͕͕̘̳̜ͦ͑͑͊̇͐͢͝ͅǪ̣̳̜̱͉̥̩̳̬̽̆͐̊ͯ͗͜͢ͅṷ̶̴̶̧̧̨̖̘̻̖̗͙̪̠̬̩͈̱̦̈́ͯ́ͧ̂ͤ͌̆̿̈́̍̀̓̍ͦ͋̿̓ͩͮ͠ͅ S̷̶̴̡̛̭̙̝̖̮͓̱̯͍͎͔̯͐̉̈̀̂̏̍̄̅́̉ͯ̂ͪ͢͢ĥ̸̵̡̡̝̺͚̤̝̫̗͕̳̬̬̘̬͍͚͇ͦͥ͌͆̀̾ͥ̀͋ͧͪ͆̄ͬͮ̽ͦ̄̕͟͡ͅO̸̧̲̝͓͍̳̗̟̟̳̼͓̘͉͖͈̟̬̊ͫ̂ͪ̒ͩ́̈́ͧͧ̑ͨ̌̽ͫ̓͠Ư̶̶̸̴̵̴̧̡̲͚̟̦̮̗̣̳̪̤̟̝͚̰̖̻̜̹̥̭͌ͨ̊͆̋̽͆̐ͦ̔̽̈͛̓͋̆͟͡L̡̲̫̹ͣͤ̀ͬ͠͞ͅD̫̲͕͕̒̐ͯ̽͊̍͢_̳̼̟̗̤͖͈͚ͬͪ̌̋͑͋͠_͙͍͙̥̓̔ͨ̌̾'̵̷̱͉̖͖̤̻̜̙̤̩̞̱̪ͧ̒̑̓̏͗ͯ̓ͯ̽̿̄ͧͨ̽̕n͐͐̇̓͛ͫͨ̒̕̚T̸̵ b̴̶̸̛̪̘͕͍͔̭͙̙͖̠͇̖ͬ́͑̄ͦ̍̔̊̀̋ͦͮ͆͠͡é Ḣ̴̳͓͉͚̜̪̜̠̼̱͌͆̅͐̈ͤͪ͐ͧͩ̃ͮ̓͘̕̕ͅE͖̔̏̅_̷̡̛̛͉͇̺̖̖̦͉̼̜̣̦̟̖̑ͥ͋̃̽ͧ̈ͨ̈́ͩ̊̆͋̂̋͐̈̒̕̚͠͝R̷̡̢̢̩̪̲̣̱̮͈̗̣̽͒͌͒̍ͪ͆͌͋̔̈̑͊̚͘͢Ḙ̵̛͉̒͒ͯ̎͗̎̅̍ͤ͜.̷̴̴̸̨͔̩̞̭͔͙̳̜̤̤̭͔͚͔͕͕̫́ͪ̍͊̓͗ͭ̃ͪͦͦͬ̇ͫͦ̋̔̂͘̕͠͝͝.̧̩͕͍͈̋ͭ̏̎ͬͫ̿̐̆̐̂̚.̴̵̴̨̡̢̼͎̯̲̳̗͖̩̲̱̙̝͎̝̳̅ͫ́ͥͯͧ̑͌ͩ͊̌̌́̋͐̚͘̚.̶̼̟͈͍̺͊ͫ̾̓́̊ͥ͜͠͠.̸̨̛̲̫̙̯͚ͣ̋̏̉̓͆̃ͨ̉ͦ̑͌͟ͅ") #Search up a scary font and use it for the creature in this chapter
                    time.sleep(1)
                    print("y̯̣̼_̢̡̨̞̘̟̼͕͕̘̳̜ͦ͑͑͊̇͐͢͝ͅǪ̣̳̜̱͉̥̩̳̬̽̆͐̊ͯ͗͜͢ͅṷ̶̴̶̧̧̨̖̘̻̖̗͙̪̠̬̩͈̱̦̈́ͯ́ͧ̂ͤ͌̆̿̈́̍̀̓̍ͦ͋̿̓ͩͮ͠ͅ S̷̶̴̡̛̭̙̝̖̮͓̱̯͍͎͔̯͐̉̈̀̂̏̍̄̅́̉ͯ̂ͪ͢͢ĥ̸̵̡̡̝̺͚̤̝̫̗͕̳̬̬̘̬͍͚͇ͦͥ͌͆̀̾ͥ̀͋ͧͪ͆̄ͬͮ̽ͦ̄̕͟͡ͅO̸̧̲̝͓͍̳̗̟̟̳̼͓̘͉͖͈̟̬̊ͫ̂ͪ̒ͩ́̈́ͧͧ̑ͨ̌̽ͫ̓͠Ư̶̶̸̴̵̴̧̡̲͚̟̦̮̗̣̳̪̤̟̝͚̰̖̻̜̹̥̭͌ͨ̊͆̋̽͆̐ͦ̔̽̈͛̓͋̆͟͡L̡̲̫̹ͣͤ̀ͬ͠͞ͅD̫̲͕͕̒̐ͯ̽͊̍͢_̳̼̟̗̤͖͈͚ͬͪ̌̋͑͋͠_͙͍͙̥̓̔ͨ̌̾'̵̷̱͉̖͖̤̻̜̙̤̩̞̱̪ͧ̒̑̓̏͗ͯ̓ͯ̽̿̄ͧͨ̽̕n͐͐̇̓͛ͫͨ̒̕̚T̸̵ b̴̶̸̛̪̘͕͍͔̭͙̙͖̠͇̖ͬ́͑̄ͦ̍̔̊̀̋ͦͮ͆͠͡é Ḣ̴̳͓͉͚̜̪̜̠̼̱͌͆̅͐̈ͤͪ͐ͧͩ̃ͮ̓͘̕̕ͅE͖̔̏̅_̷̡̛̛͉͇̺̖̖̦͉̼̜̣̦̟̖̑ͥ͋̃̽ͧ̈ͨ̈́ͩ̊̆͋̂̋͐̈̒̕̚͠͝R̷̡̢̢̩̪̲̣̱̮͈̗̣̽͒͌͒̍ͪ͆͌͋̔̈̑͊̚͘͢Ḙ̵̛͉̒͒ͯ̎͗̎̅̍ͤ͜.̷̴̴̸̨͔̩̞̭͔͙̳̜̤̤̭͔͚͔͕͕̫́ͪ̍͊̓͗ͭ̃ͪͦͦͬ̇ͫͦ̋̔̂͘̕͠͝͝.̧̩͕͍͈̋ͭ̏̎ͬͫ̿̐̆̐̂̚.̴̵̴̨̡̢̼͎̯̲̳̗͖̩̲̱̙̝͎̝̳̅ͫ́ͥͯͧ̑͌ͩ͊̌̌́̋͐̚͘̚.̶̼̟͈͍̺͊ͫ̾̓́̊ͥ͜͠͠.̸̨̛̲̫̙̯͚ͣ̋̏̉̓͆̃ͨ̉ͦ̑͌͟ͅ")
                    time.sleep(1)
                    print("y̯̣̼_̢̡̨̞̘̟̼͕͕̘̳̜ͦ͑͑͊̇͐͢͝ͅǪ̣̳̜̱͉̥̩̳̬̽̆͐̊ͯ͗͜͢ͅṷ̶̴̶̧̧̨̖̘̻̖̗͙̪̠̬̩͈̱̦̈́ͯ́ͧ̂ͤ͌̆̿̈́̍̀̓̍ͦ͋̿̓ͩͮ͠ͅ S̷̶̴̡̛̭̙̝̖̮͓̱̯͍͎͔̯͐̉̈̀̂̏̍̄̅́̉ͯ̂ͪ͢͢ĥ̸̵̡̡̝̺͚̤̝̫̗͕̳̬̬̘̬͍͚͇ͦͥ͌͆̀̾ͥ̀͋ͧͪ͆̄ͬͮ̽ͦ̄̕͟͡ͅO̸̧̲̝͓͍̳̗̟̟̳̼͓̘͉͖͈̟̬̊ͫ̂ͪ̒ͩ́̈́ͧͧ̑ͨ̌̽ͫ̓͠Ư̶̶̸̴̵̴̧̡̲͚̟̦̮̗̣̳̪̤̟̝͚̰̖̻̜̹̥̭͌ͨ̊͆̋̽͆̐ͦ̔̽̈͛̓͋̆͟͡L̡̲̫̹ͣͤ̀ͬ͠͞ͅD̫̲͕͕̒̐ͯ̽͊̍͢_̳̼̟̗̤͖͈͚ͬͪ̌̋͑͋͠_͙͍͙̥̓̔ͨ̌̾'̵̷̱͉̖͖̤̻̜̙̤̩̞̱̪ͧ̒̑̓̏͗ͯ̓ͯ̽̿̄ͧͨ̽̕n͐͐̇̓͛ͫͨ̒̕̚T̸̵ b̴̶̸̛̪̘͕͍͔̭͙̙͖̠͇̖ͬ́͑̄ͦ̍̔̊̀̋ͦͮ͆͠͡é Ḣ̴̳͓͉͚̜̪̜̠̼̱͌͆̅͐̈ͤͪ͐ͧͩ̃ͮ̓͘̕̕ͅE͖̔̏̅_̷̡̛̛͉͇̺̖̖̦͉̼̜̣̦̟̖̑ͥ͋̃̽ͧ̈ͨ̈́ͩ̊̆͋̂̋͐̈̒̕̚͠͝R̷̡̢̢̩̪̲̣̱̮͈̗̣̽͒͌͒̍ͪ͆͌͋̔̈̑͊̚͘͢Ḙ̵̛͉̒͒ͯ̎͗̎̅̍ͤ͜.̷̴̴̸̨͔̩̞̭͔͙̳̜̤̤̭͔͚͔͕͕̫́ͪ̍͊̓͗ͭ̃ͪͦͦͬ̇ͫͦ̋̔̂͘̕͠͝͝.̧̩͕͍͈̋ͭ̏̎ͬͫ̿̐̆̐̂̚.̴̵̴̨̡̢̼͎̯̲̳̗͖̩̲̱̙̝͎̝̳̅ͫ́ͥͯͧ̑͌ͩ͊̌̌́̋͐̚͘̚.̶̼̟͈͍̺͊ͫ̾̓́̊ͥ͜͠͠.̸̨̛̲̫̙̯͚ͣ̋̏̉̓͆̃ͨ̉ͦ̑͌͟ͅ")
                    time.sleep(3)
                    Inventory.reset_inventory()
                    time.sleep(3)
                    print("You wake up back at the starting point...")
                    time.sleep(3)
                    chapter_one() #Restart chapter 1 because the player has lost
                    return
            elif choice ==3:
                print("Player (Dane Miller) enters room 264")
                time.sleep(3)
                print("Dane Miller finds a room full of tools though, it doesn't seem like he'll need them")
                time.sleep(6)
                print("\"These tools prove useful but... I lack the strength to use them, it feels like since I woke up, I've been feeling very weak, why?\"")
                time.sleep(3)
                print("\"I'll leave now..\"")
                time.sleep(3)
                continue
            elif choice ==4:
                print("Player (Dane Miller) enters room 263")
                time.sleep(3)
                print("The player (Dane Miller) finds an operating room for managing certain assembly rooms but requires power")
                time.sleep(6)
                print("\"I feel like I've been here before but WHY don't I remember....why, what happened here?, why am I here? I'm so alone.. So weak, Father I wish you were here to guide me...\"")
                time.sleep(5)
                print("\"Maintain yourself Dane! The only one who can help me is myself..\"")
                time.sleep(5)
                print("\"Am I talking to myself? I must be going crazy\"")
                time.sleep(2)
                print("\"I'm leaving\"")
                time.sleep(4)
                continue #Back to list
            elif choice ==5:
                print("Player (Dane Miller) returns back to the Main Hall")
                chapter_one()
                return
            elif choice ==6:
                print("Player (Dane Miller) moves to the end of the corridor to reveal another series of rooms")
                time.sleep(3)
                print("Moving to Chapter 3")
                time.sleep(3)
                chapter_three()
                return
                
            else:
                print("Choose a number from the list: ")
    
        except ValueError:
            print("Choose a number from the list 1-6")

def chapter_three():
    print("Chapter 3: The Blue Smog")
    time.sleep(3)
    print("You notice a strange blue smog approaching from the end of the corridor, the smog looks dangerous")
    time.sleep(3)
    print("This smog isn't going anywhere but it's staring at you, waiting for you to do something...")

    while True:
            continue_yes = input("Type 'yes' to continue: ").strip().lower()
            if continue_yes == 'yes':
                break

    #Show options from the chapter 3 flowchart while also adding check inventory
    options = [
        "Check Inventory",
        "Enter room 230", 
        "Yell 'Hello' toward the smog",  
        "Continue forward"
    ]

    Key_Obtained = False

    while True: 

        for index, str in enumerate(options):
            print(f"{index+1}.{str.capitalize()}")

        try:
            choice = int(input("Choose an action from the list: "))
            if choice ==1:
                Inventory.show_inventory()# Show inventory
                continue
            elif choice ==2:
                    if not Key_Obtained:
                        time.sleep(2)
                        print("You entered room 230, the room looks worn down, still, maybe something useful here?") #"Enter room 230 (Find a key)"
                        time.sleep(3)
                        print("You have obtain a Key for a certain room") 
                        time.sleep(4) #time delay
                        print("\"A key? this one seems to be different compared to the rest I walked past\"")
                        Key_Obtained= True #Key is set true after clicking choice
                        Inventory.add_item("Key")
                        print("")#spacer
                        time.sleep(2)
                    else:
                        print("")
                        print("\"Same place nothing new now, but the smell is getting worse, what is it anyway? The smog? Smells different\"")
                        print("")
                        time.sleep(3)
                    continue
            elif choice ==3:
                time.sleep(2)
                print("You yell across the corridor") #"Yell 'Hello' toward the smog"
                time.sleep(3)
                print("You feel like yelling might get you a response from the smog? Maybe someones on the other side")
                time.sleep(3)
                print("You start hearing crackling noises, the same ones who have been staring at you since the beginning of your hopeless venture")
                print("Your flashlight begins to flicker")
                time.sleep(6)
                print("After a while nothing happens and the crackling of shadows return to their hiddens worlds")
                time.sleep(4)
                print("\"I need to get out of here, quickly\"")
                time.sleep(3)
                continue
            elif choice ==4:
                if "Gas Mask" in Inventory.inventory: # Check if Gas Mask is in inventory
                    print("")#spacer
                    print("You move forward towards the smog with your mask on.")
                    print("")#spacer
                    time.sleep(2)
                    chapter_four()
                    return
                else:
                    print("You move forward risking your life, wondering what your doing is right")
                    time.sleep(3)
                    print("You inhale the smog as you pass through")
                    print("BAD CHOICE...")
                    time.sleep(3)
                    print("Bad choices make for bad rewards, you fall onto your knees with your lungs burning and eyes, afterwards the crackling noises emerge from their shadowry worlds..")
                    time.sleep(7)
                    print("The creatures are in full view now")
                    time.sleep(3)
                    print("All the creatures laugh at you as you falter...")
                    time.sleep(3)
                    print("Before you meet the light, you notice that one of the creatures faces looks oddly similar to a co-worker")
                    time.sleep(7)
                    print("Have you seen this person before? How is this specific creature resembling human features?")
                    time.sleep(4)
                    print("")#spacer for the weird font
                    print("G̴̪̺͍͆̋ͬͪ_͌͘o̝ͥͩ̀Ǫ̶͓̠ͦͫͩ͌̕_̵̸̴̰̩̲̹̠͈̳̞̺̼̻̖̟̫̔́ͪͩ̐͂̃̅̊̏ͣ͢d̷̛̛̛̪͕̘̗̤͓̤̞͍̺̺̙̭͓͖̰̘̻͇͍͐̐͆̍ͩ̒͋̍̌̀̾ͤ͛ͮ͛͌̑͗̕͘͜N̸̵̸̢̡̪̳̹͉͈̤͖̹̩̩̑̽ͪ͌̓ͣ͐͌́̍͂̈̉̚͘͡ͅī̧̡̱̜̺̫̤̻̃ͩ͂̎̊̒̃̀͞ͅg̵̷͉͖̭̥͊ͭͭ͌͝H̱͙̩̤̦ͣ͛̂̏͛_̨̲̩͔̣̠̑̂́̒́ͧ̀͑̏̂̿̀ͥ̾̕͜Ṱ̴̨͎͈͕̪̯̫̬̣̙̠̥͓̻ͦ͊ͮ̎̎̿̊͜͞͝")
                    print("")
                    time.sleep(3)
                    print("The End")
                    Inventory.reset_inventory()# Clear progress after loss
                    chapter_one()#Restart the game from Chapter 1
                    return
            else:
                print("Choose a number from the list:")
    
        except ValueError:
            print("Choose a number from the list 1-4")

def chapter_four():
    print("Chapter 4: The Collapse")
    print("After you passed the smog with the gas mask, you feel a litle dizzy but soon wears off")
    time.sleep(3)
    print("You pay attention to the surroundings of this corridor and it's terrible")
    time.sleep(3)
    print("The corridor is completely destroyed with one or two rooms intact")
    print("There's a big hole in the middle with no end, you wonder, \"What happened here!?\"")
    print("On the side of the corridor, there's another opening which could show a way out")
    time.sleep(5)
    print("What should you do?")

    while True:
            continue_yes = input("Type 'yes' to continue: ").strip().lower()
            if continue_yes == 'yes':
                break
    
    options = [
        "Jump down the hole", 
        "Find room 199 (One of the two rooms that're intact)", 
        "Move along the path toward the outside"
    ]

    Map_Obtained = False

    while True:
        
        for index, str in enumerate(options):
            print(f"{index+1}.{str.capitalize()}")

        try:
            choice = int(input("Choose an action from the list: "))

            if choice ==1:
                print("Jumping down the hole might prove silly")
                print("Do you still wish to jump down? Even though it might be a bad idea?")
                time.sleep(2)
                confirm = input("Are you sure you want to jump down the hole? (yes/no): ").strip().lower()
                if confirm == "yes": #if yes the player loses
                    print("You decide to jump down the hole...")
                    time.sleep(2)
                    print("The fall is deeper than you expected.")
                    time.sleep(3)
                    print("The fall leads to a giant machinery room filled with acid and smog")
                    print("The color resmebles that of the crystal you saw at the beginning")
                    print("You fall onto the acidic surface and you falter")
                    time.sleep(3)
                    print("The End")
                    time.sleep(3)
                    Inventory.reset_inventory()  # Clear progress on death
                    chapter_one()  # Restart the game from Chapter 1
                    return  # Exit Chapter 4
                elif confirm == "no":#if no the player lives and returns to list
                    print("You step back from the edge of the hole")
                    continue #Return to the options list
                else:
                    print("Please answer 'yes' or 'no'.")
                    continue #Ask the question again
            elif choice ==2:
                # Find room 199 (Requires a key)
                if "Key" in Inventory.inventory:
                    if not Map_Obtained:
                        print("You use the key to unlock room 199.")
                        time.sleep(2)
                        print("Inside, you find documents about Dane Miller's past, revealing details about your connections to the factory.")
                        time.sleep(5)
                        print("\"I don't understand...why is my name here? I don't remember anything...I have to remember something right?\"")
                        time.sleep(5)
                        print("Dane Miller stares at the papers for minutes, wanting to know the truth about the past, his past self")
                        time.sleep(5)
                        print("He'll never find out as he suffered brain damage before he awoke, thus losing most of his memories")
                        time.sleep(5)
                        print("...")
                        time.sleep(2)
                        print("No answers but more questions")
                        print("Once again, as Dane Miller starts to lose hope, what is his goal in this perdicament?\" Why don't I remember any of this?\" you mutter, again and again.")
                        time.sleep(7)
                        print("Dane Miller finally exits the room with more sorrow and confusion than before")
                        print("Also, Dane Miller found a map layout of the Factory within the collection of papers")
                        Map_Obtained = True
                        time.sleep(3)
                        Inventory.add_item("Map")
                        print("")#spacer
                    else:
                        time.sleep(2)
                        print("....Dane Miller is slient....")
                        time.sleep(3)
                    continue #Go back to option list
                else:
                    print("The door to room 199 is locked. You need a key to proceed.")
                continue  #Go back to the options list
            elif choice ==3:
                print("Dane's mental state is worsening but a way out might make him feel better")
                time.sleep(5)
                print("Dane Miller proceeds")
                time.sleep(2)
                print("Moving to chapter 5")
                chapter_five()
                return
            else:
                print("Choose a number from the list:")

        except ValueError:
            print("Choose a number from the list 1-3")

def chapter_five():
    print("Chapter 5: The End Of The World")
    time.sleep(3)
    print("The sky")
    time.sleep(3)
    print("The far away buildings")
    time.sleep(3)
    print("The scream of isolation, the roaming of shadows")
    time.sleep(3)
    print("The Wainwright Factory is in complete disarray and everything around it, whatever happened cause the world to rot")
    time.sleep(3)
    print("The only thing left now is Dane Miller and the creatures that stalk him in his hopeless venture")
    time.sleep(3)
    print("The only thing now is to choose what fate is better for him")
    time.sleep(4)
    print("")#spacer
    print("Ẁ̨̢͕̤̟͙͖̤͚̰̟͋̋ͧ̏͋ͪͩ͋̚͟h̲̍͜Ą̷̛̼͎̭̗͈͇̳̪͂͒̃͆̍ͯͯ̂ͨ̈́̊Ṫ͚̪̺̀ͮ͢ S̶̷̻͇̤̗̯̲͉̺̗͈̜̬̯̩̽̈́̌̅ͩ͐̅ͪ͗͐̓̾̐̆ͤ̄͌̐͘͘͟h̷̗̮̣ͮ̃̓͐O̡̝̠̣̭̥̟͇͈͓̓̎̓̌̓̀͐͋̇͘͟ͅu̢̢̡̙͓̞̙͓̣̥͕͇̜̳̍̎̊ͥ̊͋ͬͤ̑ͭ̈́̎L̸̴̛̛̝̬̪͍̟͈̱͚̪͈̰̭̤͕̬̅̋ͬ͒̓ͬ̓̔ͪ͋̄̓́̍͂̈́̈̔̆̾ͨͮ̿̑͟d̴̶̤̘̯̅ͫ̿̾̑̍ͧ̄ͮ̅̋͝͠ ÿ̢͚̦ͧ̔͋̈O̴̜̰̭̭̽̍͡Ȗ̸̸̷̼̮͕̤͔̫̱̺̪̰̮̞̖͊͛̇ͤ͋ͭ̒ͧ̈́̑͝ d̷͍̯̮͋̆͋͑͘o͇̼̖͓̣͛̿ͦ́̕͞ͅ ṇ̖͎̥͑̂̽̃̊̿̏̇̌͝o̶͉͈͍̞͔̭̫̟̩̲͇ͤ̔ͤ̉͒̄̽̾̚͟͞Ẅ̷̱̳͙̲̥̥͖̺͖̳̤̳́ͦ̔̓ͯ̊͒̎̇̕͟?̸̨̛̹̳̲̭̘̯͎̥͖̙͚̏ͧͤ̈͟͜͞ͅ N̢̡̻̭̫͎̪͔̣͚̲̗͕̫͕̝̲͙̄̿ͭ̓́̀̓͑͌͗ͪ̑͐ͭ̍͊̏́̎͆̂ͫ̎͘͜͝ͅͅo̷̵̙̺̤̫̬͇̹̜̗͚̟̍ͯ̆ͨ̇̾͒̏̑́͛ͣ̆̃̌ͤͤ͆ͅ w̨̫̥͉̰̘̫̮̘̪͉̟̦͍̌̓̔ͦͦͭͭ́̉ͣͫͦ̈́̕̕͘͜͞ͅḥ̫̥̞̽̓͌e̴̢̢̛̮̘̳̲̗̲̣̤ͦͪ͑ͨ̍ͦ͆̇̆̅̃̍͗ͥͯ̾̽̓̀͐́̃̕̕͜͜͟͟r̷̛̜̫̫͔̗̘̎̉̿̌͂͗̿ͭ̉̾ͬ̾̑ͮ̕͢͢͟͝ͅͅE̴̢̡̬̞͕̜̦̲̱̣͓̬̙͎̘̭̙͔ͭ͛͊ͭ̿ͪ͊̈ͥ̓̈̊̌ͬ͒̂̍̉ͥ t͕͠Ȍ̶̸͙͙̜͓͚ͥ̀ͪ̏̿̽ͩ̀̉͑̅͌ r̸̵̡̧͚̳̱̟͉̳͖͚͙̞ͣ̃ͭ̆̽̊ͯ̽ͦ̀̓͂̌ͮ̅̈͒͟U̷̴̵̡̠͔̫̠͇͉̹̮̝͕ͧ̀̍ͯͣ̃ͩ͐̌͊̎̄ͯͯņ̡̛̛̛̦̩͕͕̮͙̣͎͖͇̜͎̮̤͓̻ͮ̉̎̇͛͋́ͨ̒͆́̃ͧͪͦ̈́͜͝͞͠ͅ t̤̤͔̖̤̱̬̱̹̤̯̱͈͍̓ͪͦ̉̽̿̔̑ͯ̐̇̒̓̐̚͝͡o̒_̴̼̭̼̇̃͌̉͐̀ͥͧ̋͌̿̊͞ n̸̢̝͈̽̔ͬ̀̕_̧̤̳͈̬̅̀̇̈̊ͫ͂ͨ̚ͅO̶̶̼͙͙̖͍͙̺̦̱͗ͧ̂̎̑ͦ͊ͨ̑̾͂w.̧̫͝.̢̡̩̘͉̰͕̤̱͍̹ͩ̈ͦ̓̀́̓́ͨͦͩ̏͊̈ͧ̕")
    print("")#spacer
    time.sleep(5)

    while True:
            continue_yes = input("Type 'yes' to continue: ").strip().lower()
            if continue_yes == 'yes':
                break

    options = [
        "Yell for a response", 
        "Run away from the place (Map required)", 
        "Go back inside to find potential solutions"
    ]

    while True:

        for index, str in enumerate(options):
            print(f"{index+1}.{str.capitalize()}")

        try:
            choice = int(input("Choose an action from the list: "))

            if choice ==1:
                print("You yell into the wasteland, hoping for some kind of response from other potential survivors but your the only one...")
                time.sleep(5)
                print("Crackling sounds emerge from the shadows, but nothing else happens.")
                time.sleep(3)
                print("The silence fills the atmosphere as you stand there.")
                time.sleep(3)
                continue #Return to the options list
            elif choice ==2:
                if "Map" in Inventory.inventory:
                    print("Using the map you will try to manage a way out of the factory considering its size")
                    time.sleep(6)
                    print("The factories complexity, you want to hope that there's survivors just like you")
                    time.sleep(6)
                    print("The experience of humans is to struggle and move forward, create soltuions, and find ways to overcome")
                    time.sleep(6)
                    print("Dane, as sad as he is, he won't let this place be his grave, he'll carry on")
                    time.sleep(6)
                    print("\"The time I've lost, my injured body, even so...I must try, to live and overcome this wretched place, find anew peace...\"")
                    time.sleep(6)
                    print("...")
                    time.sleep(4)
                    print("True Ending: Overcome and Believe")
                    time.sleep(2)
                    Inventory.reset_inventory()
                    chapter_End()
                    return
                else:
                    print("You try to run away, but without a map, the factory stretches endlessly in every direction...")
                    time.sleep(5)
                    print("The Factory is very large and complex, used for mass production of energy resources from the unknown crystal")
                    time.sleep(5)
                    print("It's important to have a map, if not, many get lost")
                    time.sleep(3)
                    print("...")
                    time.sleep(3)
                    print("Exhausted and lost, Dane Miller collapses to the ground, the shadowry creatures emerge and Dane falters")
                    time.sleep(2)
                    print("Bad Ending: No escape")
                    time.sleep(5)
                    Inventory.reset_inventory()#Clear progress on death
                    chapter_End() #create a def that just says thank for playing my game, etc
                    return  #Exit Chapter 5
            elif choice ==3:
                print("Dane Miller goes back inside the factory maybe hoping for some resources, that'll help him")
                time.sleep(4)
                print("It could be a bad idea considering that more shadowry creatures are becoming more abundant the more he stays")
                time.sleep(4)
                print("Maybe Dane Miller will previll against the creatures?")
                time.sleep(4)
                print("Potential medicine even..")
                time.sleep(4)
                print("Might be a good ending or bad ending depending on Dane")
                time.sleep(4)
                print("To be continued...")
                time.sleep(4)
                print("Odd Ending: Playing with the dice of life")
                time.sleep(2)
                Inventory.reset_inventory()#Clear progress on death
                chapter_End() #create a def that just says thank for playing my game, etc
                return#Exit Chapter 5

            else:
                print("Choose a number from the list:")

        except ValueError:
            print("Choose a number from the list 1-3")

def chapter_End():
    print("Hello!")
    time.sleep(3)
    print("Thank you for playing my game!")
    time.sleep(3)
    print("It took awhile to create this adventure game, around 15 plus hours or so?")
    time.sleep(3)
    print("It was kinda hard to make, so I used a combination of videos, etc which include")
    print("Bro code (Youtuber), google searches, announcement videos, milestone 3 example, flow chart, and milestone 1")
    time.sleep(3)
    print("Hope you enjoy it, take care")
    time.sleep(5)
    exit()

chapter_one()