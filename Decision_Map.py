from Sentence import*

from Loading import*
from Dictionary import*
from PC import*
from Checks import*
from Battle import*

#This will will handle all decisons which require user input or interaction

class Talihu_Decisons():

    class Yalids_inn():

        lexicon = Talihu_dict().Yalids_inn()
        room_set = False
        # stores which skills have been used to prevent the user using the same skill more than once in a given senario.
        # Also when a particular skill is performed it may mean that another skill can't be used.
        skill_performed = []

        information_gathered = False

        def choose_room_or_bar(self):
            print("~ Welcome to 'Yalids Inn' Sir ~"),sec(3)
            print("\n~ We have manys rooms to cater to all needs ~"),sec(3)
            print("\n~ also some of the best food and ale in the city. ~"),sec(3)
            print("\n~ I'm 'Yalid ~"),sec(2)
            print("\n~ How may I be of service? ~"),sec(2)

            tuple = Sentence_Handler().scanner(self.lexicon.room_or_bar,'sentence')
            lists = (self.lexicon.get_room, self.lexicon.go_bar)

            methods = (self.get_room, self.go_bar)
            parameters = []
            checks = (2,2,0)

            Sentence_Handler().word_filter( checks, tuple, lists, 'sentence', methods, parameters)

        def get_room(self):

            print("~ That's fine sir ~"),sec(2)
            print("\n~ Do you know what kind of room you'd like? ~"),sec(2)

            tuple = Sentence_Handler().scanner(self.lexicon.room_yes_no,'simple')
            lists = (self.lexicon.room_yes, self.lexicon.room_no)

            methods = (self.room_yes_or_no)
            parameters = ['yes','no']
            checks = [2,1,2]

            Sentence_Handler().word_filter(checks, tuple, lists, 'simple', methods, parameters)

        def room_yes_or_no(self,response):


            if response == 'no':
                print('~ Well we have four types of rooms ~'),sec(2)
                print('\n~ Small rooms come with a Single bed. ~'),sec(2)
                print("\n~ Medium rooms come with a Double bed. ~"),sec(2)
                print("\n~ Large rooms come with a King size bed and en-suite ~"),sec(2)
                print("\n~ The Queen's rooms is our biggest. ~"),sec(2)
                print("\n~ It's a fully furnished apparment with two rooms. ~"),sec(2)
                print("\n~ both have Queen size beds. ~"),sec(2)



            print("\n~ Which one would you like? ~"),sec(2)
            tuple = Sentence_Handler().scanner(self.lexicon.choose_room,'simple')
            list=(self.lexicon.single_room,self.lexicon.double_room,self.lexicon.large_room,self.lexicon.queen_room)

            method=(self.set_room)
            parameters =('Small'),('Medium'),('Large'),('Queen\'s')
            checks = (4,1,4)

            Sentence_Handler().word_filter( checks, tuple, list, 'simple', method,parameters)


        def set_room(self,parameters):
            size = parameters


            if self.room_set is False:
                print("~ Sure ~")
                print("\n~ We're going to get the {} room ready for you ~".format(size)),sec(2)
                print("\n~ It shoudldn't take too long ~"),sec(2)
                print("\n~ But while we get everything prepared why don't you head towards the bar. ~"),sec(3)
                prompt()
                self.go_bar()
                self.room_set= True

            elif self.room_set is None:
                print("~ Sure ~")
                print("\n~We have a {} room ready for you ~".format(size)),sec(2)
                print("\n~ If you'd like to follow me ~")
                self.room_set = True




        def go_bar(self):



            print("\n~ The bar is just on your left ~")

            prompt()
            print("> You walk in the direction of the Bar "),sec(2)
            print("\n> Observing the pictures dotted across the wall "),sec(2)
            print("\n> You pay particular attention to one which depicts The Great War "),sec(3)
            print("\n> In the distance you hear a few people "),sec(2)
            print("\n> They seem to be enbrawled in a heated debate "),sec(2)
            print("\n> As you near the mouth of the dinning area a scrawny man approaches "),sec(2)
            print("\n> He is wearing a black pin strip jacket with matching trouser "),sec(2)
            print("\n> On the jacket there is an emblem that of Yalid's Inn "),sec(2)
            print("\n> The man greets you. "),sec(2)
            prompt()
            print("\n~ Good evening {} ~".format(PC['Character']['Name'])),sec(2)
            print("\n~ I'm Gorno I'll be your server today ~"),sec(3)
            print("\n~ Please follow me and I'll have you seated ~"),sec(2)
            prompt()
            print("> Gorno gudies you to a table next to a window"),sec(2)




        def get_more_information(self):

            skill_performed = self.skill_performed

            intimidation = self.lexicon.get_more_information_with_intimidation
            persuasion =  self.lexicon.get_more_information_with_persuasion
            preception = self.lexicon.get_more_information_with_preception


            if "Preceptionn" in skill_performed:
                dict = {**persuasion,**intimidation}

            elif 'Persuasion' in skill_performed:
                dict = {**intimidation}

            elif "Preception" in skill_performed and 'Persuasion' in skill_performed:
                dict = {**intimidation}

            else:
                dict = {**intimidation,**persuasion,**preception}



            tuple = Sentence_Handler().scanner(dict,'skill')
            lists = (self.lexicon.intimidation,self.lexicon.persuasion,self.lexicon.preception)

            methods = (Checks().skill_check)
            parameters = [
            ('Intimidation','Hard',self.get_more_information_with_intimidation,'D20'),
            ('Persuasion','Medium',self.get_more_information_with_persuasion,'D20'),
            ("Preception",'Easy',self.get_more_information_with_preception,'D20')
            ]
            checks=(3,1,3)

            Sentence_Handler().word_filter(checks,tuple,lists,'skill',methods,parameters)

        def get_more_information_with_preception(self,condition):
            #print(f"You've rolled a {roll_total}")
            prompt()
            print("> You move closer to their table."),sec(2)
            print("\n> facing towrads the stage as to appear discrete"),sec(2)
            print("\n> You listen intently to thier conversation"),sec(2)

            if condition is True:
                prompt()
                print("|Ork| ~ I couldn't do anything ~ "),sec(2)
                print("\n|Ork| ~ There were to many of them ~"),sec(2)
                print("\n|Human 1| ~ You're paid to protect us and our goods ~"),sec(2)
                print("\n|Human 3| ~ He's right, you should of atleast tried ~"),sec(2)
                print("\n|Ork| ~ Then we'd all be dead ~"),sec(2)
                print("\n|Human 2| ~ Damn Resistance ~"),sec(2)
                print("\n|Human 1| ~They'll get what's coming, don't worry ~"),sec(2)
                prompt()
                print("> It appears that your assumption was correct"),sec(2)
                print("\n> It was the work of the resistance"),sec(2)
                print("\n> You need to find out thier location"),sec(2)




            else:
                prompt()
                print("> You're unable to hear enough."),sec(2)
                print("\n> Over the music playing "),sec(2)
                print("\n> You need to try somehting else"),sec(2)

            self.skill_performed.append("Preception")
            self.get_more_information()

        def get_more_information_with_persuasion(self,condition):
        #    print(f"You've rolled a {roll_total}")
            prompt()
            print("> You head to their table"),sec(2)
            prompt()
            print("* I couldn't help but over ear your conversation *"),sec(2)
            print("\n* Did you have some trouble coming into the city? *"),sec(2)

            if condition is True:
                prompt()
                print("|Human 2| ~ If you can call it that ~"),sec(2)
                print("\n|Human 3| ~ We were heading to the Citadel ~"),sec(2)
                print("\n|Human 3| ~ on business for the Chancellor. ~"),sec(2)
                print("\n|Human 3| ~ We had very important cargo to deliver ~"),sec(2)
                print("\n|Human 2| ~ Out of nowhere them scraggly bastards ~"),sec(2)
                print("\n|Human 2| ~ with a face only a mother could love ~"),sec(2)
                print("\n|Human 2| ~ popped up ~"),sec(2)
                skip()
                print("\n|Human 2| ~ They took everything ~"),sec(2)
                print("\n|Human 1| ~ Even the god damn trailer ~"),sec(2)
                print("\n|Human 1| ~ and that miserable prick just there"),sec(2)
                print("\n|Human 1| ~ You had one bloody job ~"),sec(2)
                print("\n> Pointing to the ork"),sec(2)
                print("\n|Human 1  ~ Protect us and the cargo ~"),sec(2)
                print("\n|Human 2| ~ Definetly failed misserably ~"),sec(2)
                prompt()
                print("* Who did it? *"),sec(2)
                prompt()
                print("|Human 3| ~ Don't play coy with us. ~"),sec(2)
                print("\n|Human 1| ~ It was them. ~"),sec(2)
                print("\n|Human 1| ~ The resistance ~"),sec(2)
                prompt()
                print("* Are you sure? *"),sec(2)
                print("|Human 2| ~ Yes were fucking sure ~"),sec(2)
                prompt()
                print("* I need you to tell me exacttly where  this happened *"),sec(2)
                prompt()
                print("|Human 2| ~ Hold up, ~"),sec(2)
                print("\n|Human 2| ~ Who the fuck are you ~"),sec(2)
                prompt()
                print("* Me? *"),sec(2)
                print("\n* I'm {}".format(PC["Character"]["Name"])),sec(2)
                prompt()

                if PC["Character"]["Name"] == "Lord Elkas":
                    print("|Human 2| ~ Please forgive me my  Lord ~"),sec(2)
                    print("\n|Human 2| ~ I meant no offense we've just had a bit of a day ~"),sec(2)
                    prompt()
                    print("* Just tell me what I want to know *"),sec(2)
                    prompt()
                else:
                    print("|Human 1| ~ Your a noisy little bugger ain't ya ~"),sec(2)
                    prompt()
                    print("* Not at all *"),sec(2)
                    print("\n* I'm in search for the people who've brought you such misfourtune *"),sec(2)
                    print("\n* Tell me what need to know and you can continue drowning your sorrows *"),sec(2)
                    prompt()
                print("|Human 3| ~ Of course, . ~"),sec(2)
                print("\n|Human 3| ~ We were coming down Lapque ~"),sec(2)
                print("\n|Human 3| ~ They jumped out on us near Lillies River"),sec(2)
                prompt()
                print("* Thank thank you *"),sec(2)
                print("\n* Enjoy the rest of your eveining "),sec(2)
                prompt()
                print("> You head back towards your table"),sec(2)
                self.information_gathered = True
                self.get_rest()




            else:
                prompt()
                print("|Human 2| ~ I think you should mind your own business ~ "),sec(2)
                prompt()
                print("> Being polite didn't work well"),sec(2)
                print("\n> You need to try something else"),sec(2)

                self.skill_performed.append("Persuasion")
                self.get_more_information()




        def get_more_information_with_intimidation(self,condition):

            if  "Persuasion" not in self.skill_performed:
                prompt()
                print("> You head to their table"),sec(2)
                prompt()
                print("* I hear you lads got into a bit of pickle *"),sec(2)
                print("\n* Now for reasons I can't be bothered to explain *"),sec(2)
                print("\n* I need to know what happened and where *"),sec(2)
                print("\n* Don't waste my time *"),sec(2)



            if condition is True:
                prompt()
                print("|Human 3| ~ Of course, . ~"),sec(2)
                print("\n|Human 3| ~ We were coming down Lapque ~"),sec(2)
                print("\n|Human 3| ~ The Resistance took our trailer and all our stuff ~"),sec(2)
                print("\n|Human 3| ~ They jumped out on us near Lillies River"),sec(2)
                print("\n|Human 2| ~ We're lucky to be alive ~"),sec(2)
                prompt()
                print("* I'd say *"),sec(2)
                prompt()
                print("\n> You head back to your table")
                self.get_rest()
            else:


                prompt()
                print("|Ork| ~ Your brave little sod ~"),sec(2)
                print("\n|Human 1| ~ Go fuck yourself ~"),sec(2)
                prompt()
                print("> You've tried to intimidate the group not the best idea given thier numbers"),sec(3)
                print("\n> The ork has become defensive and get's up from his seat."),sec(2)
                print("\n> With a weapon in hand")

                prompt()
                outcome = Battle("Jurafa").encounter()
                sec(3)
                prompt()
                if outcome == "Fight Difused":
                    print("* I'm not looking to cause any trouble *"),sec(2)
                    print("\n* Just needed to be pointed in the right direction"),sec(2)
                    print("\n* But I'll figure it out. *"),sec(2)
                    prompt()
                    print("> You've avoided having a fight"),sec(2)
                    prntt("\n> You move towrds your table"),sec(2)
                    self.information_gathered = False


                elif outcome == "PC Dead":
                    print("> You suffer a slow and painfull death"),sec(2)
                    self.information_gathered = None

                    #Call Check Point


                elif outcome == "NPC Dead":
                    print("> The death of their comrad has made them very talkative"),sec(2)
                    prompt()

                    print("|Human 3| ~ We were coming down Lapque ~"),sec(2)
                    print("\n|Human 3| ~ The Resistance took our trailer and all our stuff ~"),sec(2)
                    print("\n|Human 3| ~ They jumped out on us near Lillies River"),sec(2)
                    print("\n|Human 2| ~ We're lucky to be alive ~"),sec(2)
                    prompt()
                    print("* Right you are *"),sec(2)
                    print("\n* Sorry about your friend he was a little full of himself *"),sec(2)
                    self.information_gathered = True


                elif outcome == "NPC Unconsious":
                    print("> Thier unconious guard is lying next to them"),sec(2)
                    print("\n> They seem ready to start talking"),sec(2)
                    prompt()
                    print("* So where were we? *"),sec(2)
                    prompt()
                    print("|Human 3| ~ We were coming down Lapque ~"),sec(2)
                    print("\n|Human 3| ~ They jumped out on us near Lillies River"),sec(2)
                    print("\n|Human 3| ~ The Resistance they took our trailer and all our stuff ~"),sec(2)
                    print("\n|Human 2| ~ We're lucky to be alive ~"),sec(2)
                    prompt()
                    print("* Right you are"),sec(2)
                    print("\n* I'd higher a few extra guards next time *"),sec(2)
                    print("\n* This ones definetly no good *"),sec(2)
                    self.information_gathered = True



                elif outcome == "PC Revived":
                    print("> You took alot of damage to continue fight would be risky"),sec(2)
                    print("\n> You return back to your table."),sec(2)
                    self.information_gathered = False

                self.get_rest()


        def get_rest(self):
            prompt()
            print("> You sit down at your table contemplating what step you'll take next."),sec(2)
            print("\n> Gorno burst's through the kitchen doors with a tray in hand"),sec(2)
            print("\n> Heading in your direction"),sec(2)
            print("\n> As he gets closer the smell of Gibly Pie intensifies"),sec(2)
            print("\n> He places the food and drink on your table."),sec(2)
            prompt()
            print("~ I hope you enjoy your meal. ~"),sec(2)

            if self.information_gathered == False:

                print("\n~ Do forgive me"),sec(2)
                print("\n~ I couldn't help but over hear you enquiring about the merchants mishap ~"),sec(2)
                print("\n~ I heard them talking to Yalid about how they were ambushed ~"),sec(2)
                print("\n~ He might be able to help ~"),sec(2)
                prompt()
                print("* Wonderful *"),sec(2)
                print("\n* I appreciate your assistance in the matter *"),sec(2)
                print("\n* Thank you *"),sec(2)
                prompt()
                print("~ Your weclome ~"),sec(2)

            prompt()
            print("> The Gibly Pie is good."),sec(2)
            print("\n> You finish your meal rather quick"),sec(2)
            print("\n> You continue to think whilst listening to the melody"),sec(2)
            print("\n> It's getting late, you need to get some sleep"),sec(2)

            if (self.room_set is True) and (self.information_gathered is False):

                print("\n> Yalid approaches your table"),sec(2)
                prompt()
                print("~ Good evening sir your room is ready ~"),sec(2)
                print("\n~ If you'd like to follow me ~"),sec(2)
                prompt()
                print("* Sure. *"),sec(2)
                print("\n* I wondered if you could help me with a little problem *"),sec(2)
                print("\n* I hear the resistance have been operating in the area *"),sec(2)
                print("\n* Have you heard anything *"),sec(2)
                prompt()
                print("~ Yes I have unfortunaly"),sec(2)
                print("\n~ They've been opperating near Lillies River ~"),sec(2)
                print("\n~ Down by Lapque ~"),sec(2)
                prompt()
                print("* Thank you I appreciate the help *"),sec(2)
                self.information_gathered = True


            elif (self.room_set is False) and (self.information_gathered is False):

                print("\n> You head out of the bar back towards the reception"),sec(2)
                print("\n> Yalid is standing behind the table. "),sec(2)
                prompt()

                print("* I wondered if you could help me with a little problem *"),sec(2)
                print("\n* I hear the resistance have been seen in the area *"),sec(2)
                print("\n* Have you heard anything *"),sec(2)
                prompt()
                print("~ Yes I have unfortunaly"),sec(2)
                print("\n~ They've been sighted near Lillies River ~"),sec(2)
                print("\n~ Down by Lapque"),sec(2)
                prompt()
                print("* Thank you *"),sec(2)
                print("\n* I also need a room if you'd be so kind *"),sec(2)
                prompt()

                self.room_set = None
                self.information_gathered = True

                self.get_room()


            elif (self.room_set is False) and (self.information_gathered is True):

                print("\n> You head out of the bar back towards the reception"),sec(2)
                print("\n> Yalid is standing behind the table. "),sec(2)
                prompt()
                print("* I wondered if you could help me *"),sec(2)
                print("\n* I need a room if you'd be so kind *"),sec(2)

                self.room_set = None
                self.get_room()


            elif (self.room_set is True) and (self.information_gathered is True):

                print("\n> Yalid approaches your table"),sec(2)
                prompt()
                print("~ Good evening sir your room is ready ~"),sec(2)
                print("\n~ If you'd like to follow me ~"),sec(2)


            prompt()
            print("\n> You follow Yalid up a few flights of stairs"),sec(2)
            print("\n> He stops on the four floor"),sec(2)
            print("\n> and guides you to your room"),sec(2)
            prompt()
            print("~ This is your room I hope you have a good rest ~"),sec(2)
            prompt()
            print("* I will thank you sir *"),sec(2)
            prompt()
            print("> You enter the room and have a quick look around"),sec(2)
            print("\n> then make yout way to the bed, you take a seat on the edge. "),sec(2)
