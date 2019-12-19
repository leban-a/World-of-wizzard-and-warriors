from PC import PC
from NPC import NPC
from Die import Die
from Checks import Checks
from random import randint
from Sentence import Sentence_Handler
from Dictionary import *
from Loading import*


# The Battle class will handle enconters with enimies.
class Battle():

    # When Initiated NPC (Non Player Character) name has to be supplied
    def __init__(self,name):
        self.NPC_Name = name


    fight = True  # Used to determine if a fight will begin

    # Initiative determines which player will have the first move when  fight begins
    # initiative_roll will handle the rolling mechanism.


    def action(self):
        # If PC has rolled the highest derived from Initiative they will have a number the options
        # At the moment the options are limited :

        gap()
        print("What action do you take")

        tuple = Sentence_Handler().scanner(Talihu_dict.Yalids_inn.actions,"action")  # Get sutiable Response

        # Fight : Start a fight
        if "fight" in tuple:

            self.fight = True


        # defuse: Attempt to descalate the situation - Will have to perform a skill check
        elif "defuse" in tuple:

            Checks().skill_check(('Persuasion','Hard',self.defuse,'D20'))

    # Checks condition passed by skill_check
    def defuse(self,condition):

        gap()

        if condition is  True:

            print("> You've managed to defuse the situation"),sec(2)
            self.fight = False


        elif condition is False:

            print("> You failed to defuse the situation, your going to have to fight"),sec(2)
            self.fight = True

    # PC battle control.
    def PC_battle(self):

        sec(4)
        prompt()
        gap()

        player = "PC"

        print("It's your turn\n"),sec(2)


        #
        while True:

            print("Choose a weapon"),sec(2)
            tuple = Sentence_Handler().scanner(PC["Weapons"],"weapon") # Checks against PC Weapons Dict
            weapon = tuple[4].capitalize() # Weapon is stored at point 4 in tuple.

            # Non Mele type weapons will usually have a set number
            # Example: 4 Arrows

            try:  # Checks if the choosen weapon has a "Count" attribute

                if PC["Attacks and Spells"][weapon]["Count"] > 0:
                    PC["Attacks and Spells"][weapon]["Count"] -= 1
                    break
                else: # IF weapon count is at 0 player will have to choose a differnt weapon
                    print(f"You have no remaining {weapon}'s")
                    gap()
            except: # If attribute not found in dict loop will break
                break






        atk_bonus = PC["Attacks and Spells"][weapon]["Atk Bonus"]

        attack =  Die().attack_roll(NPC[self.NPC_Name]["Armour Class"], player, self.NPC_Name,atk_bonus)


        if attack is True:

            die = PC["Attacks and Spells"][weapon]["Damage"]["Die"]
            rolls = PC["Attacks and Spells"][weapon]["Damage"]["Rolls"]
            bonus = PC["Attacks and Spells"][weapon]["Damage"]["Bonus"]

            damage = Die().hit_roll(die,rolls,bonus,player,self.NPC_Name)

            prompt()

            NPC[self.NPC_Name]["Hit Points"]["Current"] +=  damage

            NPC_remaining_Hit_Points = (NPC[self.NPC_Name]["Hit Points"]["Max"])-(NPC[self.NPC_Name]["Hit Points"]["Current"])

            if NPC[self.NPC_Name]["Hit Points"]["Current"] > NPC[self.NPC_Name]["Hit Points"]["Max"]:

                NPC_additional_Hit_Points = ( NPC[self.NPC_Name]["Hit Points"]["Max"] - NPC[self.NPC_Name]["Hit Points"]["Current"]) * -1

                print("{} has: 0 remaining Hit Points".format(self.NPC_Name)),sec(2)
                print("\nand has taken an additional damage of: {} Hit Points ".format(NPC_additional_Hit_Points)),sec(2)
                print("\n{}'s current health is at {}".format(self.NPC_Name,NPC_remaining_Hit_Points))


            else:

                print("{}'s has: {} remaining Hit Points ".format(self.NPC_Name,(NPC_remaining_Hit_Points)))

    #NPC - Battle control, all actions performed are automated
    def NPC_battle(self):

        sec(4)
        prompt()
        gap()

        player = "NPC"

        # Weapon Selection
        while True:

            random_weapon = randint(0,(len(NPC[self.NPC_Name]["Weapons List"])-1))      # genterates a random number depending on the number of items stored in the Weapons list.

            weapon = NPC[self.NPC_Name]["Weapons List"][random_weapon] # Weapon selected using the number provided by randoom_weapon

            try: # Checks if the choosen weapon has a "Count" attribute
                if NPC[self.NPC_Name]["Attacks and Spells"][weapon]["Count"] > 0:
                    NPC[self.NPC_Name]["Attacks and Spells"][weapon]["Count"] -= 1
                    break
                 # IF weapon count is at 0 loop restarts
            except: # weapon has no count attribute loop breaks
                break



        atk_bonus =  NPC[self.NPC_Name]["Attacks and Spells"][weapon]["Atk Bonus"]

        print("It's {}'s turn".format(self.NPC_Name)),sec(2)
        gap()

        attack =  Die().attack_roll(PC["Stats"]["Armour Class"],player,self.NPC_Name,atk_bonus)

        if attack == True:

            die = NPC[self.NPC_Name]["Attacks and Spells"][weapon]["Die"]
            rolls = NPC[self.NPC_Name]["Attacks and Spells"][weapon]["Rolls"]
            bonus = NPC[self.NPC_Name]["Attacks and Spells"][weapon]["Bonus"]

            damage = Die().hit_roll(die,rolls,bonus,player,self.NPC_Name)

            prompt()

            PC["Stats"]["CHP"]["Current"] +=  damage

            PC_remaining_Hit_Points = (PC["Stats"]["CHP"]["Max"]-PC["Stats"]["CHP"]["Current"])


            if PC["Stats"]["CHP"]["Current"] > PC["Stats"]["CHP"]["Max"]:

                PC_additional_Hit_Points = (PC["Stats"]["CHP"]["Max"] - PC["Stats"]["CHP"]["Current"]) * -1

                print("You have: 0 remaining Hit Points"),sec(2)
                print("\nand have also taken an additional damage of: {} Hit Points ".format(PC_additional_Hit_Points)),sec(2)
                print("\nYou current health is at {}".format(PC_remaining_Hit_Points))


            elif PC["Stats"]["CHP"]["Current"] <= PC["Stats"]["CHP"]["Max"]:
                print("You have: {} remaining Hit Points".format(PC_remaining_Hit_Points))





    # encounter will simulate a the battle between the PC and NPC:
    def encounter(self):

        start = Checks().initiative_check(self.NPC_Name) # fight order determined

        if start == "PC":

            self.action() # PC chooses to fight or defuse the situation


        if self.fight == True:   # fighting starts



            # Loop will run unitl a character's Hit Point is <= 0.
            while (PC["Stats"]["CHP"]["Current"] <PC["Stats"]["CHP"]["Max"]) and (NPC[self.NPC_Name]["Hit Points"]["Current"] < NPC[self.NPC_Name]["Hit Points"]["Max"]):

                    if start == "PC": # PC will start the attack

                        self.PC_battle() # PC's turn to attack

                        if NPC[self.NPC_Name]["Hit Points"]["Current"] >= NPC[self.NPC_Name]["Hit Points"]["Max"]: # Checks if while loop condition is met for NPC
                            break


                        self.NPC_battle() # NPC's turn to attack

                    elif start == "NPC": # NPC will start the attack

                        self.NPC_battle()

                        if PC["Stats"]["CHP"]["Current"] >= PC["Stats"]["CHP"]["Max"]: # Checks if will loop contion is met for PC
                            break


                        self.PC_battle()
            prompt()
            # Depending on who won the battle and how a differnt action will be called.
            if  (PC["Stats"]["CHP"]["Current"] == PC["Stats"]["CHP"]["Max"]):
                print("You've fallen unconsious")
                outcome =  Checks.death_saving_throw()

            elif (PC["Stats"]["CHP"]["Current"] > PC["Stats"]["CHP"]["Max"]):
                print("You've been killed")
                outcome = "PC Dead"

            elif (NPC[self.NPC_Name]["Hit Points"]["Current"] == NPC[self.NPC_Name]["Hit Points"]["Max"]):
                print("You've  knocked {} unconsious".format(self.NPC_Name))
                outcome = "NPC Unconsious"

            elif(NPC[self.NPC_Name]["Hit Points"]["Current"] > NPC[self.NPC_Name]["Hit Points"]["Max"]):
                print("You've killed {}".format(self.NPC_Name))
                outcome = "NPC Dead"

            return outcome




        elif self.fight == False: # Fight was not intiated as 'action' resulted in a postive response.
            outcome = "Fight Disfused"
            return outcome
