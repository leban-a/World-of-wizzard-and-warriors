from random import randint
from Loading import  *



class Die():  # Handles all actions which utilize a Dice Roll

    critical_hit = False

    # dice_list will store the differnt types of dice
    dice_list = {
    'D4':4,
    'D6':6,
    'D8':8,
    'D10':10,
    'D12':12,
    'D20':20
    }
    # Each task which is perfomred will have a differnt difficulty. which will be a random rumber within the difficulty range.
    difficulty_list={
    "Very Easy":(randint(1,5)),
    "Easy":(randint(6,10)),
    "Medium":(randint(11,15)),
    "Hard":(randint(16,20)),
    "Very Hard":(randint(21,25)),
    "Imposible":(randint(26,30))
    }

    def roll(self,die): # roll acts as a dice

        roll = randint(1,self.dice_list.get(die))
        return roll

    def skill_roll(self,skill,difficulty,die): # skill check performed

        print("The difficulty for this task is set to {}".format(difficulty)),sec(2)

        difficulty = self.difficulty_list.get(difficulty)
        print("\nYou need to roll a number equal to or above {}".format(difficulty)),sec(2)
        gap()
        print("Perform Skill Check"),sec(2)
        input("#"),sec(4)

        roll = self.roll('D20')

        print(f"\nYou've rolled a {roll} with a proficiency of {skill}")


        roll_total = roll + skill



        if roll_total >= difficulty:
            condition = True
        else:
            condition = False

        return (condition)

    def initiative_roll(self,PC_bonus,NPC_bonus,NPC_Name):



        tie = False
        while True:  # Loop once as long as "tie" remains False
            if tie == True:
                prompt()
                print("It's a Tie"),sec(2)
                gap()


            # PC initiative Roll
            print("Perfrom a Initiative Check"),sec(2)
            input("#")
            roll = self.roll('D20')
            print("\nYou've rolled a {} with Proficiency of {}".format(roll,PC_bonus)),sec(2)

            PC_roll_total = roll + PC_bonus

            prompt()

            #NPC initiative Roll
            print("{} will perform an Initiative Check".format(NPC_Name)),sec(4)
            roll = self.roll('D20')


            print("\n{} rolled a {} with a Proficiency of {}".format(NPC_Name,roll,NPC_bonus)),sec(2)


            NPC_roll_total = roll + NPC_bonus

            if NPC_roll_total == PC_roll_total:
                tie = True
            else:
                break




        prompt()

        if NPC_roll_total > PC_roll_total:    #sets who will act first.
            print("{} rolled highest".format(NPC_Name)),sec(2)
            return 'NPC'
        else:
            print("You've rolled the highest"),sec(2)
            return 'PC'

    def attack_roll(self,difficulty,player,NPC_Name,atk_bonus): # Used to to determine if an attack succeds or fails.

            if player == "PC":

                print("{} has a Armour class of {}".format(NPC_Name,difficulty)),sec(2)
                gap()
                print("Perform an Attack Roll"),sec(2)
                input("#"),sec(4)


                roll = self.roll('D20')
                print(f"\nYou've rolled a {roll} with an Attack Bonus of {atk_bonus}"),sec(2) #" with a proficiency of {skills_main.get(skill)}""")


                roll_total = roll + atk_bonus
                if roll == 1:
                    print("\nYou've missed")
                    condition = False

                elif (roll_total >= difficulty):
                    print("\nThus succeding in breaking through {}'s armour".format(NPC_Name)),sec(2)
                    condition = True
                else:
                    print("\nThus failing to break through {}'s armour".format(NPC_Name))
                    condition = False


            elif player == "NPC": # NPC actions will be automated

                roll=self.roll("D20")

                print("{} will perform an Attack Roll".format(NPC_Name)),sec(4)

                print("\n{} has rolled a {} with an Attack Bonus of {}".format(NPC_Name,roll,atk_bonus)),sec(2)
                roll_total = roll + atk_bonus

                if roll == 1:
                    print("\nYou've missed")
                    condition = False

                elif (roll_total >= difficulty):
                    print("\nThus succeding in breaking through your armour".format(NPC_Name)),sec(2)
                    condition = True
                else:
                    print("\nThus failing to break through your armour".format(NPC_Name))
                    condition = False

            if roll >= 20:
                self.critical_hit = True




            return condition

    def hit_roll(self,die,rolls,bonus,player,NPC_Name): # Used to determine the amount of damage PC or NPC recieves.

            damage = 0

            if self.critical_hit == True:
                self.critical_hit = False

                rolls +=  1

                gap()
                print("Critical Hit!!")

                if player == "PC":
                    print("\nYou've gained an additional Hit Roll"),sec(2)
                elif player == "NPC":
                    print("\n{} has gained an additional Hit Roll".format(NPC_Name)),sec(2)


            if player == "PC":

                count = 0
                while count < rolls:
                    count +=  1
                    gap()
                    print("Perform Hit Roll"),sec(2)
                    input("#"),sec(4)


                    roll = self.roll(die)


                    print("\nYou've rolled a {}".format(roll)),sec(2)
                    damage +=  roll


                total_damage = damage + bonus
                print("\nYou've dealt a total of {} Hit Points".format(total_damage))
                return total_damage

            elif player == "NPC":

                gap()
                print("{} will will perform an Hit Roll".format(NPC_Name)),sec(4)

                count=0
                while count != rolls:
                    count +=  1

                    roll = self.roll(die)

                    print("\n{}'s rolled a {}".format(NPC_Name,roll)),sec(4)
                    damage += roll




                total_damage = damage + bonus
                print("\n{} has dealt a total of {} Hit Points".format(NPC_Name,total_damage))
                return total_damage

    def death_saving_throw(self,PC_health):


        prompt()
        print("Your Hit Points have fallen to 0")
        print("\nYou have to peform a Death Saving Throw")


        successes = ["O","O","O"]
        failures =  ["O","O","O"]

        saves = 0
        fails = 0



        while (saves != 3) and (fails != 3):
            sec(3)
            gap()
            print("Perform Saving Throw")
            input("#")

            saving_throw = Die().roll('D20')

            sec(2)
            gap()
            print("You've Rolled a {}\n".format(saving_throw)),sec(2)

            if saving_throw == 20:
                print("You've regained 1 Hit Point")
                PC_health  +=  1
                successes[saves] = "X"
                saves +=  1

            elif saving_throw == 1:
                print("You've gained two fails")
                failures[fails]=("X")
                fails = fails + 1
                if fails != 3:

                    failures[fails] = "X"
                    fails +=  1


            elif saving_throw >= 10:
                print("That's a success")
                successes[saves] = ("X")
                saves += 1
            else:
                print("That's a fail")
                failures[fails] = ("X")
                fails +=  1

            sec(2)
            gap()
            print("Successes: {}".format(successes))
            sec(0.2)
            print("\nFailures:  {}".format(failures))


        if saves == 3:
            PC_health =+ 1


        return PC_health
