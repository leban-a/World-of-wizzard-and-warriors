from PC import PC, skills_main
from NPC import NPC
from Die import Die
from Loading import*

# When playing various checks will have to performed.
# These checks will usually require the player to roll a die.


class Checks():

    def skill_check(parameters): # skill_check determines if a player is succesful at an attempt to perform a certain action.

        # multiple paramters will always be passed in the form of a tuple:

        skill = skills_main[parameters[0]] # which skill will be checked
        difficulty = parameters[1] # diffuclty of the task to be performed
        method = parameters[2] # function which will be used after the check is complete.
        die= parameters[3] # type of die used

        check_roll = Die().skill_roll(skill,difficulty,die)

        (method)(check_roll)



    def initiative_check(NPC_Name):# Initiative determines which player will have the first move when fight scene begins

        #Initiative Bonus
        PC_initiative =  PC["Stats"]["Initiative"]
        NPC_initiative = NPC[NPC_Name]["Dexterity"]["Modifier"]

        start = Die().initiative_roll(PC_initiative,NPC_initiative,NPC_Name)

        return start

    def death_saving_throw(): # When PC falls unconsious death saving throw will be called giving the player a chance to restore some hit points.

        current_Hit_Points = PC["Stats"]["CHP"]["Current"]

        health = Die().death_saving_throw(current_Hit_Points)


        prompt()

        if health == 0:

            print("You've failed to restore any Hit Points")
            return "PC Dead"

        else:

            print("You've regained {}".format(health))
            return "PC Revived "
