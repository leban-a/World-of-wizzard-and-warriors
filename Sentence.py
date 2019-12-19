from Loading import*

class Sentence_Handler():

    def sort_words(sentence,lexicon): # Checks words against Lexicon list, then pairs the key and values

        result = [] #Match words store in a list.
        words = sentence.lower().split() #split sentence and converts to lower

        for word in words: #cycles through list of split words.

            word = self.string_to_int(word)   #cheks if the word can be converted to a number.

            if word in lexicon: #checks "word" against the lexicon

                word_type = lexicon[word]  #gets the value of the "word"
                pair = (word, word_type) # pairs "word" & "word_type" in a tuple/
                result.append(pair) #adds pair to the result list.

            else: #if word is not in the lexicon

                if (len(result) == 0) and  (word in ["i" ,"i'm" ,'im' ,'am']): #checks if the word refers to first person

                    pair = (word,'subj')
                    result.append(pair)

                elif isinstance(word,1): # checks if the word is of type int

                    pair = (word,'number')
                    result.append(pair)

                else: #all other words will be treated as stop words. which will later be ignored

                    pair = (word,"stop")
                    result.append(pair)

        return result

    def string_to_int(word): # converts "str" to "int": str("One") and str("1")  to int(1)


        #if word in Dictionary.numbers:    # number in word form to int
        #    word = Dictionary.numbers[word]

        try:  #number in str form to int
            return int(word)
        except ValueError:
            return word

    def parser(word_list,sentence_type):  #checks the sorted words and converts them into a usable sentence.
        # type of sentence being looked at: different setences will have different requirements.


        #each of the required words will be sotred in one of these variables.
        noun = None
        verb = None
        subj = None
        direction = None
        number = None
        skill = None
        action = None
        weapon = None

        count = True # Checks if this the first instance of the loop. ie the first word in the list.

        for word in word_list:
            if (count == True) and word[1] == 'subj':
                subj = 'player'
            elif (count == True) and word[1] ==  'noun':
                subj = word[0]
            elif word[1] == 'noun':
                noun = word[0]
            elif word[1] == 'verb':
                verb = word[0]
            elif word[1] == 'direction':
                direction = word[0]
            elif word[1] == 'number':
                number = word[0]
            elif word[1] == 'skill':
                skill = word[0]
            elif word[1]== 'action':
                action = word[0]
            elif word[1] == "weapon":
                weapon =word[0]

            #if there are multiple words with the same type the last one checked will be used.

            if subj == None:
                subj = 'player'
            count = False


        # this will ensure that the correct words that are needed are present depending on setence typ

        if sentence_type == 'sentence':
            assert (verb != None),("[A verb was expected]")
            assert (noun != None),("[A noun was expected]")

        elif sentence_type == 'direction':
            assert (verb != None),("[A verb was expected]")
            assert (direction != None),("[A direction was expected]")

        elif sentence_type == 'number':
            assert (number != None),("[A number was expected]")

        elif sentence_type == 'simple':
            assert (verb != None),("[A verb was expected]")

        elif sentence_type == 'skill':
            assert (skill != None),("[A skill was expected]")

        elif sentence_type == 'action':
            assert (action != None),("[A action was expected]")

        elif sentence_type == 'weapon':
            assert (weapon != None),("[A weapon was expected]")
        gap()

        return(subj,verb,noun,skill,weapon,action,direction,number) #set of usable words returned.

    def scanner(self,lexicon,sentence_type): #combines sort_word and parser

        while  True:  # will continue to loop if user doesn't enter the required words will also inform user of the type of word that is needed
            gap()
            sentence = input("> ")
            word_list = self.sort_words(sentence,lexicon)

            try:
                phrase = self.parser(word_list,sentence_type)
                return phrase
                break
            except AssertionError as error:
                print(error)

    def word_filter(check,tuple, list, sentence_type, method, parameters):
        # Bad Code Below:
        # This is an absolute disaster.
        # At the momment it seems to serve the purpose but
        # i know it will cause a number of issues

        #tuple = subj=[0],verb=[1],noun=[2],skill=[3],weapon=[4],action=[5],direction=[6],number=[7]
        #Checks = ([0]= checks, [1] = Methods, [2] = Parameters)
        #sentence_type = type of sentence being handled

        #### These will hold multiple values depending on requirements. ######

        #list = stores accepted words   [list[0],list[1],list[2]

        #method =  function which will be executed   [method[0],method[1],method[2]]

        #parameters =  parameters to be supplied    [paramters[0],paramters[1],paramters[2]]

        ##################################################


        # So this method will user the result from scanner. "tuple"
        # depending on sentence_type certain points will be checked in the tuple.
        # this mehtod allows me to check the tuple against differnt lists if a match is found
        # the appopraite method will be called with paramters if assigned.

        # list, method and paramters can contain multiple valuse,
        # the first value in each will be used in the first check. then the program will move on to the second value in the set.
        #checks tell the program how many lists are being checked, the number of methods being used and number of parameters
        # depending on the number of methods used and parameters differnt checks will be performed.



        exit = -1  # control when the program exits.

        access = -1
        #access will contol what values are being used in each check.
        # first check will use all values stored at [0] then second check [1] and so on.


        while exit != (check[0] - 1): # loop will exit once all checks are performed or when a match is found

            access = access + 1  #

            exit = exit + 1

            if   ( (check[1] > 0) and (check[2] == 0) ):  # Takes multiple Methods and no parameters

                if sentence_type == 'sentence':

                    if tuple[0] == 'player':

                        if (tuple[1] in list[access]) and (tuple[2] in list[access]):

                            (method[access])()
                            break


                    else:

                        if (tuple[0] in list[access]) and (tuple[1] in list[access]):

                            (method[access])()
                            break

                elif sentence_type == 'simple':

                        if tuple[0] == 'player':

                            if (tuple[1] in list[access]) and (tuple[2] in list[access]):

                                (method[access])()
                                break

                            elif tuple[1]  in list[access]:

                                (method[access])()
                                break

                        else:

                            if (tuple[0] in list[access]) and (tuple[1] in list[access]):

                                (method)[access]()
                                break

                            elif (tuple[1] in list[access]) and (tuple[2] in list[access]):

                                (method[access])()
                                break

            elif ( (check[1] == 1) and (check[2] > 0) ):   # Takes one Method and Multiple Parameters

                if sentence_type == 'skill':

                    if tuple[0] == 'player':


                        if (tuple[1] in list[access]) and (tuple[3] in list[access]):

                            (method)(parameters[access])
                            break

                        elif tuple[3]  in list[access]:

                            (method)(parameters[access])
                            break

                    else:

                        if (tuple[0] in list[access]) and (tuple[3] in list[access]):

                            (method)(parameters[access])
                            break

                        elif (tuple[1] in list[access]) and (tuple[3] in list[access]):

                            (method)(parameters[access])
                elif sentence_type == 'simple':
                    if tuple[0] == 'player':

                        if (tuple[1] in list[access]) and (tuple[2] in list[access]):

                            (method)(parameters[access])
                            break

                        elif tuple[1]  in list[access]:

                            (method)(parameters[access])
                            break

                    else:

                        if (tuple[0] in list[access]) and (tuple[1] in list[access]):

                            (method)(parameters[access])
                            break

                        elif (tuple[1] in list[access]) and (tuple[2] in list[access]):

                            (method)(parameters[access])
                            break
            elif( (check[1] > 1) and (check[2] > 1) ): #Takes Multiple Methods and Multiple Parameters

                if sentence_type == 'sentence':

                    if tuple[0] == 'player':

                        if tuple[1] and tuple[2] in list[access]:

                            (method)(parameters[access])
                            break

                        else:

                            if (tuple[0] in list[access]) and tuple[1] in list[access]:

                                (method[access])(parameters[access])
                                break



                elif sentence_type == 'simple':

                    if tuple[0] == 'player':

                        if (tuple[1] in list[access]) and (tuple[2] in list[access]):

                            (method[access])(parameters[access])
                            break


                        elif tuple[1]  in list[access]:

                            (method[access])(parameters[access])
                            break

                        else:

                            if (tuple[0] in list[access]) and (tuple[1] in list[access]):

                                (method[access])(parameters[access])
                                break


                            elif (tuple[1] in list[access]) and (tuple[2] in list[access]):

                                (method[access])(parameters[access])
                                break
                elif sentence_type == 'action':


                    if tuple[0] == 'player':

                        if (tuple[5] in list[access] ):


                            (method[access])(parameters[access])
                            break
