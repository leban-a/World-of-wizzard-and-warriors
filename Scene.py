from Loading import*
from User import*
from Help import*
from PC import*
from sys import exit
from Decision_Map import*

#PC  = character_Bio[character["key"]]


class Scene(object): # Base class with single function enter().

     def enter(self):
         gap(),sec(0.5)
         gap(),sec(0.5)
         gap(),sec(0.5)
         print('This scene is not yet avalible \nBuild in progress')
         exit(100)

class Intro_Setup(Scene): # First Scene, Player name taken and they are then showed the user guide
    def enter(self):
        print("The game is loading won't be long"),sec(3)
        print("\nWhile that's happening, let's do a few things."),sec(2)

        User_Name().get_user_name()
        Help().guide()


        Characters().character_selection()

        gap()
        print("\nThats the basics done let's get down to business")
        prompt()
        load(1,1.5,None)
        return('Intro World Opening')

class Intro_World_Opening(Scene): #Player introduced to the world of Nottirel
    def enter(self):
        print("\n\t\t\t\t\tWeclome To The World Of Wizards & Warriors\n\n"),sec(2)
        gap(),sec(1)
        gap(),sec(1)
        gap(),sec(1)
        print("\nThe game is set in:"),sec(3)
        print("\nThe Land of Nottirel"),sec(3)
        print("\n\nThis is a vasts world which streaches arcoss many oceans and barren deserts"),sec(3)
        print("\nIt is generally a peacefull place since the great war."),sec(3)
        print("\nwhich almost desolated the planet"),sec(3)
        prompt()
        print("The plannet has since been been divided into many kingdoms each with its own way off life."),sec(3)
        print("\nNottirel is inhabitted by many beings spread across the countless peaks"),sec(3)
        print("\nHumans, Elves, Gobbilins and many other sentient beings."),sec(3)
        print("\nThey all call this place home"),sec(3)
        print("\nMost live harmounsly side by side"),sec(3)
        prompt()
        print("But there are a few"),sec(3)
        print("\nThey call themselves the last resistance."),sec(3)
        print("\nThey live in small pockets across the land"),sec(3)
        print("\nThey oppose the current way of life and believe they are the suppreme beings"),sec(3)
        print("\nTheir objective is simple. Start another war."),sec(3)
        print("\nBy causing annimosity bewteen the various factors"),sec(3)
        prompt()
        print("This is a land of magic and intrigue, full of violence and compassion."),sec(3)
        print("\nEvery being here has one goal to surrive and will do so by any means they belive is nessasary"),sec(4)
        print("\nIt can be a very unforgiving and relentless landscape"),sec(3)
        print("\nWith many obstacles and creatures looking for a quick bite."),sec(3)
        prompt()
        print("In this game you will have to use your wit and skills to navigate treachous world"),sec(3)
        print("\nIn the process you will have to overcome foes and assist your felow people."),sec(3)
        print("\nYour most imporant objective is to mitigate any conflicts that may arise."),sec(3)
        print("\nAs you flush out the remaining resistance "),sec(3)
        gap()
        print("We wish you the best of luck {}".format(PC["Character"]["Name"]))
        skip()
        return("Talihu")

class Talihu(Scene): # Character start point
    def enter(self):
        print("> It's early in the evening, you've arrived in the eastern district of Talihu. "),sec(3)
        print("\n> In the sixth season of Hitiri, where the weather fluctuates rapidly. "),sec(3.5)
        print("\n> You look towards the south where you can see the second moon starting to rise above a lime and violet sky. ")
        prompt()
        print("> Your walking down a cobbled path with every steep you feel the stones wobble, "),sec(4)
        print("\n> and a sligt slickness beneath ypur feet. "),sec(2)
        print("\n> One wrong step and you could find yourself in a very unpleasant situation. "),sec(3)
        print("\n> You head towards the city center "),sec(2)
        prompt()
        print("> The area around you quietens as the factories grind to a halt, "),sec(3)
        print("\n> at the same time streets begin to flood with workers, "),sec(3)
        print("\n> all rushing to get home before the evening chill hits. "),sec(3)
        print("\n> You need get your self indoors quickly "),sec(2)
        prompt()
        print("> You turn right onto Blickly Cove "),sec(2)
        print("\n> The road is packed with inns and taverns on either side. "),sec(3)
        print("\n> The buildings are mostly old and poorly kept. "),sec(3)
        print("\n> You look for one that might meet your needs. "),sec(3)
        print("\n> Near the bottom of the road you see a brightly lit Inn "),sec(3)
        print("\n> You move towards it. "),sec(2)
        prompt()
        print("> As you get closer you notice it has a intriging decor "),sec(3)
        print("\n> which resembles that of the Nagiti Tribe. "),sec(3)
        print("\n> You head to the entrance which has a great big oak door, "),sec(3)
        print("\n> held in place by salid silver, one of the strongest metals know. "),sec(3)
        prompt()
        print("\n> Above the door a sign reads Yalid's Inn. "),sec(3)
        print("\n> As you stand there admiring the craftmenship. "),sec(3)
        print("\n> The tempature starts to drop rapidly "),sec(2)
        prompt()
        print("\n* This will have to do. *"),sec(2)
        prompt()
        print("> You on knock on the door three times with a slight pause between each knock. "),sec(2)
        prompt()
        print("> The door opens "),sec(2)
        print("\n> You feel a plesant fragrance wafts over you. "),sec(3)
        print("\n> It reminds you of Gibly pie. "),sec(2)
        print("\n> A burly old man stands in the doorway "),sec(3)
        print("\n> His face is rinkled and you can tell the years havent been kind to him "),sec(2)
        prompt()
        print("> You look around the dimly lit Inn "),sec(2)
        print("\n> The place is plastered with many ornaments and trinkets "),sec(3)
        print("\n> It's mostly quite with a soothing melody playing "),sec(3)
        prompt()
        Talihu_Decisons.Yalids_inn().choose_room_or_bar()
        print("> You take a seat in an arm chair")
        print("> The bar is a little busier than you first expected.")
        print("> You look around the spacious area in the far corner there is stage")
        print("> An Elf is on a piano ")
        print("> There is a number of people gathered,")
        print("> listening intently to the female play")
        print("> Gorno returns ")
        prompt()
        Print(" ~ Are you ready to order? ~")
        prompt()
        print("* Yes *")
        print("\n* I'd like some Gibly Pie and Brown Ale")
        prompt()
        print("~ Certainly, I'll be back shortly ~")
        print("\n> Gorno abruptly heads back to the direction from which he came.")
        prompt()

        print("> The commotion which heard earlier continues")
        print("> From what you can make out they're talking about")
        print("> thier journey into the district")
        print("> There are four men gathered around the table")
        print("> An ork and three humans")
        print("> They appear to be merchants")
        print("> From the snipets of the conversation you've overheard")
        print("> It seems that they were ambushed")
        print("> Their description of the of the assailants appears to be that of a Patu")
        print("> You have it on good athoritty that resistance have been opperating in this area")
        print("> You need to find a way gather more information before you can be sure")
        prompt()
        Talihu_Decisons.Yalids_inn().get_more_information()
        prompt()
        print("> You've got a busy day ahead, It's best you try sleep")
        Talihu.Scene().enter()
