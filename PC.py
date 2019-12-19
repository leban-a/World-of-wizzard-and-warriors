from Loading import *


character = {'key':'1'} # Default character when program starts



class Characters(): #Stores Player Charaters


    def character_selection(self): # Characacter
        gap()
        print("CHARACTER SELECTION\n")
        #character = None    # Stores the character the player will play throughout the game.

        character['key'] = None  # Stores the character the player will play throughout the game
        while character['key'] == None:  # Loop exit's when character choosen

            gap()
            print("These are the avalible characters: "),sec(1)
            for level1 in character_Bio: #iterates through bio Main Key (ID) # Level represents depth when acceesing sub dict
                print('\n{}:  {}'.format(level1,character_Bio[level1]['Character']['Name'])) #prints Characters Name With ID number
            gap()
            sec(2)

            print("Which Character would you like to view?"),sec(1)

            while True: # User selects character they'd like to view
                c_input = input("\nPlease enter character ID \n> ")

                if c_input in character_Bio: #Checks if ID exists
                    gap()
                    print("Bio-\n")
                    for level3, level4 in character_Bio[c_input]['Bio'].items(): # Level represents depth when acceesing sub dict
                        print(f"\n{level3}: {level4}")
                    break
                else:
                    print(f"[ {c_input} is a invalid ID ]")  #Error invalid response
                    gap()


            prompt()
            print("Would you like to the view full profile?"),sec(1) #Requests if user would like to view a a more detailed Bio
            while True:
                more_info = input("\nYes or No \n> ")
                if more_info.lower() == 'yes':
                    self.print_C(c_input)
                    break
                elif more_info.lower() == 'no':
                    break
                else:
                    print(f"[ {more_info} is a invalid respose ]")
                    gap()

            gap()
            print("Would you like to play as {}?".format(character_Bio[c_input]["Character"]["Name"])),sec(1)
            while True:

                accept = input("\nYes or No \n> ")
                if accept.lower() == 'yes':

                    character['key'] = c_input  # Player character set
                    PC  = character_Bio[character["key"]]

                    gap()
                    print( PC["Character"]["Name"])
                    print(character['key'])
                    print(c_input)

                    break

                elif accept.lower() == 'no':
                    break
                else:
                    print (f"[ {accept} is a invalid respose ]") #Error invalid resposne
                    gap()



    def print_C(level1): # Prints entire character Bio  with some formatting
    # crlevle represents the depth when accessing sub dict's.
    #Level1 = Character ID


        for level2 in character_Bio[level1].keys(): # Level represents depth when acceesing sub dict


            if level2 in ["Weapons","Death Saves","Saving Throw","Weapon Attribute"]: # Following dicts do not need to be printed.
                pass
            else:
                gap()
                print(f"{level2} -\n")

                for level3, level4 in character_Bio[level1][level2].items():
                    print(f"\t{level3}: \n\t{level4}\n")

                skip()

# Stores the various PC's
character_Bio = {
'1':
{
"Character":{"Name":'Lord Elkas'},
"Bio":{'Full Name':'Lord Elkas Droverson', 'Class': 'Fighter', 'Level': 1, 'Background': 'Noble', 'Race': 'Human', 'Aignment': 'Lawful neutral', 'exp':0},
"Traits":{
    'Personality':
        """My Flattery makes those I talk to feel wonderful and important.\n\tAlso, I don't like to get dirty, and I won't be caught dead in unsuitable accomadation""",

     'Ideals':
         "Responsibility. It's the duty of a noble to protect the common people not bully them.",

     'Bonds':
         "My greataxe is a family heirloom, and it's by far my most precious possession",

     'Flaws':
         """I have a hard time resisting the allure of wealth, especially gold.\n\tWealth can help restore my legacy"""
},
"Features":{
    'Second Wind':
          """You have a limited well of stamina you can draw on to protect yourself from harm.\n\tYou can use a bonus action to regain hit points equal to 1d10 + your fighter level.""",

     'Fighter Style (Defense)':
          "While you are wearing armour, you gain a +1 bonus to AC. \n\tThis bonus is already included in your AC",

     'Position of Privilege':
          """Thanks to your noble birth, people are inclinded to think the best of you.\n\tYou are weclome in high society and people assume you have the right to be wherever your are.\n\tThe common folk make every effort to accomodate you and avoid your displeasure,\n\tand other people of high birth treat you as a member of the same social sphere.\n\tYou can secure an audience with a local noble if you need to."""
},
"Abilities":{
    'Strength':{'Base': 16, 'Modifier': 3},
    'Dexterity':{'Base': 9, 'Modifier': -1},
    'Constitution':{'Base': 15, 'Modifier': 2},
    'Intelligence': {'Base': 11, 'Modifier': 0},
    'Wisdom': {'Base': 13, 'Modifier': 1},
    'Charisma':{'Base': 14, 'Modifier': 2},
    'Passive Wisdom':13,
    'Inspiration': 0,
    'Proficiency Bonus': 2
},
"Skills":{
    'Strength':
        {'Athletics': 5,},
    'Dexterity':
        {'Acrobatics': -1,'Slight of hand': -1,'Stealth': -1,},
    'Constitution':
        {'Endurance': 2},
    'Intelligence':
        {'Arcana': 0, 'History': 2, 'Investigation': 0, 'Nature': 0, 'Religion': 0,},
    'Wisdom':
        {'Insight': 1, 'Medicine': 1, 'Preception': 3, 'Survival': 1},
    'Charisma':
        {'Deception': 2, 'Intimidation': 2, 'Performance': 2, 'Persuasion':4},


},
"Proficiencies":{
    'Proficiencie':{"All armour", "Sheilds", "Simple weapons", "Martial weapons", "Playing cards"},

    'Languages':{'Common','Draconic','Dwarvish'}
},
"Saving Throw":{
    'Strength': 5,
    'Dexterity': -1,
    'Constitution': 4,
    'Intelligence': 0,
    'Wisdom': 1,
    'Charisma': 2,
},
"Stats":{
    'Armour Class': 17,
    'Initiative': -1,
    'Speed': 30,
    'CHP':{'Max': 12, 'Current': 0},
    'THP': 0,
    'Hit Dice':{'Die':'D10','Rolls':1}
},
"Death Saves":{
    'Successes': 0, 'Failures': 0
},
"Weapons":
    {"greataxe":"weapon","javelin":"weapon"},

"Weapon Attribute":
{"Greataxe":"Strength","Javelin":"Dexterity"},

"Attacks and Spells":{
    "Greataxe":{'Atk Bonus':5, 'Damage':{'Die':"D12",'Rolls':1, 'Bonus': 3, 'Type':"Slashing" } },
    "Javelin":{"Count":3, 'Atk Bonus': 5, 'Damage':{'Die':"D6",'Rolls':1, 'Bonus': 3, 'Type':"Piercing" }}
},
"Equipment":{
    "Chain mail":1,
    "Greataxe":1, "Javelins":3,
    "Backpack":1, "Blanket":1, "Tinderbox":1, "Rations": 2, "Waterskin":1
},
},

'2':
{
"Character":{"Name":'Piril The Cleric'},
"Bio":{'Full Name':'Piril Sapphiredge', 'Class': 'Cleric', 'Level': 1, 'Background': 'Soilder', 'Race': 'Hill Dawf', 'Aignment': 'Neutral Good', 'exp':0},
"Traits":{
    'Personality':
        """I'm always polite and respectful.\n\tAlso, I don't trust my gut feelings, so I tend to wait for others to act.""",

     'Ideals':
         "Respect. People deserve to be treated with diginity and courtesy.",

     'Bonds':
         """I have three cousins -- Grundren, Tharden and Nundro Rockseeker,who are my freinds and cherished clan members""",

     'Flaws':
         """I secretly wonder weather the gods care about mortal affairs at all"""
 },
"Features":{
    'Spellcasting Ability':
           f"""Wisdoms is your spell casting ability for spells. The saving throw DC tp resist a spell yu cast is {13}.\n\tYour attack bonus when you make an attack with a spell is +5.\n\tSee the rule books on casting yours spells""",

    'Disciple of life':
           """Your healing spells are particualary effective. Whenever you restore hit points to a creature\n\twith a spell of 1st level ot higher, the creature regains additional hit points equal to 2 + the spell's level """,

    'Darkvision':
           """You see a dim light within a 60-foot radius of you as if it were briht light,\n\tand in darkness in that radius as if it were dim light. You can't discern color in darkness only shades of gray""",

    'Dwarven Resilience':
       """You have an advantage on saving throws against poison, and you have a resistance again poison damage""",

    'Dwarven Thoughness':
       f"""Your hit point maxiumum increases by {1} and it increase by {1} every time you gain a level.""",

    'Mercanary':
       """You were a minor officer amoung the mintarn mercenaries, a position that still gets you some perks.\n\tEven though  you're not on active duty, Mintarn soldiers recognize your authority and influence, \n\tso they defer to you\n\tif they are of a lower rank. You can requistion simple equipment and horses for temporary use.\n\tYou can also gain access to Mintarn mercenary encampments and fortresses"""
},
"Abilities":{
    'Strength':{'Base': 14, 'Modifier': 2},
    'Dexterity':{'Base': 8, 'Modifier': -1},
    'Constitution':{'Base': 15, 'Modifier': 2} ,
    'Intelligence': {'Base': 10, 'Modifier': 0} ,
    'Wisdom': {'Base': 16, 'Modifier': 3},
    'Charisma':{'Base': 12, 'Modifier': 1}
},
"Skills":{
    'Strength':
        {'Athletics': 4,},
    'Dexterity':
        {'Acrobatics': -1,'Slight of hand': -1,'Stealth': -1,},
    'Constitution':
        {'Endurance': 2},
    'Intelligence':
        {'Arcana': 0, 'History': 0, 'Investigation': 0, 'Nature': 0, 'Religion': 2,},
    'Wisdom':
        {'Insight': 3, 'Medicine': 5, 'Preception': 3, 'Survival': 3},
    'Charisma':
        {'Deception': 1, 'Intimidation': 3, 'Performance': 1, 'Persuasion':1},
    'Passive wisdom':13,
    'Inspiration': None,
    'Proficiency bonus': 2
},
"Proficiencies":{
    'Proficiencies':

        {"All Armour", "Sheilds", "All Simple Weapons", 'Battleaxe', 'Handaxe',
         'Light Hammers', 'Warhammers','\tPlaying Cards','Mason Tools', 'Land Vehicles'},


    'Languages':{'Common','Dwarvish'},

    'Stonecunning':

            """Whenever you make an intelligence (History) check related to the origin of a stonework, you are considered \n\tproficient in the History skill and add double your proficiency bonus to the check insead of the normal proficiency bonus"""

        },
"Saving Throw":{
     'Strength': 5,
     'Dexterity': -1,
     'Constitution': 4,
     'Intelligence': 0,
     'Wisdom': 1,
     'Charisma': 2,
},
"Stats":{
    'Armour Class': 17,
    'Initiative': -1,
    'Speed': 30,
    'CHP':{'max': 12, 'current': 0},
    'THP': 0,
    'Hit Dice':{'Die':'D10','Rolls':1}

},
"Death Saves":{
    'Successes': 0, 'Failures': 0
},

"Weapons":
    {"Warhammer":"weapon","Handaxe":"Weapon"},

"Weapon Attribute":
    {"Warhamer":"Strength","Handaxe":"Strength"},

"Attacks and Spells":{
    "Warhammer":{'Atk Bonus': 4, 'Damage':{'Die':"D8",'Rolls':1, 'Bonus': 2, 'Type':"Bludgeoning" } },
    "Handaxe":{ 'Atk Bonus': 4, 'Damage':{'Die':"D6",'Rolls':1, 'Bonus': 2, 'Type':"Slashing" }}
},
"Equipment":{
    "Chain mail": 1,"Shield": 1,'Warhammer': 1,
    'Holy Symbol': 1,'Backpack': 1,'Crowbar': 1,'Hammer': 1,
    "Pistons":10, "Torches":10, "Tinderbox": 1, "Ration":10, 'Waterskin': 1,
     "Hempen Rope": 50, "Masons Tools": 1,"Dagger": 1,"Playing Cards": 1,"Common Clothes": 1,
     "Pouch": 1, "Rank-Insignia":"(Sergeant)"
}

}
}

PC  = character_Bio[character["key"]] # PC will be used wheneven charcter attributes from "character_Bio" # "character" holds PC ID





# dict used to access PC Attributes # Will mainly used by Die.skill_check
skills_main = {
"Athletics":PC["Skills"]["Strength"]["Athletics"],

"Acrobatics":PC["Skills"]["Dexterity"]["Acrobatics"],
"Slight of hand":PC["Skills"]["Dexterity"]["Slight of hand"],
"Stealth":PC["Skills"]["Dexterity"]["Stealth"],

"Endurance":PC["Skills"]["Constitution"]["Endurance"],

"Arcana":PC["Skills"]["Intelligence"]["Arcana"],
"History":PC["Skills"]["Intelligence"]["History"],
"Investigation":PC["Skills"]["Intelligence"]["Investigation"],
"Nature":PC["Skills"]["Intelligence"]["Nature"],
"Religion":PC["Skills"]["Intelligence"]["Religion"],

"Insight":PC["Skills"]["Wisdom"]["Insight"],
"Medicine":PC["Skills"]["Wisdom"]["Medicine"],
"Preception":PC["Skills"]["Wisdom"]["Preception"],
"Survival":PC["Skills"]["Wisdom"]["Survival"],

"Deception":PC["Skills"]["Charisma"]["Deception"],
"Intimidation":PC["Skills"]["Charisma"]["Intimidation"],
"Performance":PC["Skills"]["Charisma"]["Performance"],
"Persuasion":PC["Skills"]["Charisma"]["Deception"],
}



# follwing dict's used for a "passive skill check", that does not require the player to roll.
skills_basic = {
"Strength":PC["Abilities"]["Strength"]["Base"],
"Dexterity":PC["Abilities"]["Dexterity"]["Base"],
"Constition":PC["Abilities"]["Constitution"]["Base"],
"Intelligence":PC["Abilities"]["Intelligence"]["Base"],
"Wisdom":PC["Abilities"]["Wisdom"]["Base"],
"Charisma":PC["Abilities"]["Charisma"]["Base"],
"Passive Wisdom":PC["Abilities"]["Passive Wisdom"],
"Inspiration":PC["Abilities"]["Inspiration"],
"Bonus":PC["Abilities"]["Proficiency Bonus"]
}

skills_modifier = {
"Strength":PC["Abilities"]["Strength"]["Modifier"],
"Dexterity":PC["Abilities"]["Dexterity"]["Modifier"],
"Constition":PC["Abilities"]["Constitution"]["Modifier"],
"Intelligence":PC["Abilities"]["Intelligence"]["Modifier"],
"Wisdom":PC["Abilities"]["Wisdom"]["Modifier"],
"Charisma":PC["Abilities"]["Charisma"]["Modifier"],
"Passive Wisdom":PC["Abilities"]["Passive Wisdom"],
"Inspiration":PC["Abilities"]["Inspiration"],
"Bonus":PC["Abilities"]["Proficiency Bonus"]
}
