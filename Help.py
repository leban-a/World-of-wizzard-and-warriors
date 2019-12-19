from Loading import *

class Help(): # Gudies related to playing the game and walkthroughs



    def guide(): #User is provided the option to view help guides for the game


        gap()
        print("Would you like to view the Help Guides?\n"),sec(0.5)
        while True: #Exit's when correct answer is given
            response = input ("Yes or No \n> ")
            #User response checked
            if response.lower() == 'yes':
                self.load_guide() #Run Load Guide
                break

            elif response.lower() == 'no':
                break

            else: # If invalid response is provide error is displayed. While loop return to the top.
                print(f'[ {response} is a invalid response ]')
                gap()

    def load_guide(self): #User selects which guide they want to view
        gap()
        print("Which guide would you like to view\n"),sec(0.5)
        while True:

            for manual in self.manuals: # iterates through guides stored in 'manual' dictionary
                print (f"{manual}",end =', ') # prints 'manuals' keys
            guide_input = input("\n> ") # user prompted to enter the guide they wish to view
            if guide_input.capitalize() in Help.manuals: # user input is checked against manual key's / User's input is converted to capitalize
                gap()
                guide = (self.manuals[(guide_input.capitalize())])() #guide called using users input

                break
            else:
                print(f"[ {guide_input} is not valid Guide ]")
                gap()

    def manual(): #will be added at a later date
        print("\nThis is the Manual\n")


        skip()
        Help.guide()

    def introduction(): #will be added at a later date
        print("\nThis is the Introduction\n")

        skip()
        Help.guide()

        #Game Guides stored in dictionary
    manuals= {'Manual':manual,'Introduction':introduction}
