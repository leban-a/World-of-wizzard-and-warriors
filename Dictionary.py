
class Talihu_dict():

    class Yalids_inn(object):

        # How may I be of service?: Room or Bar>
        room_or_bar = {
        'room':'noun',
        'rooms':'noun',
        'bed':'noun',
        'shower':'noun',
        'beds':'noun',
        'food':'noun',
        'drink':'noun',
        'bar':'noun',
        'table':'noun',
        'thirsty':'verb',
        'get':'verb',
        'sleep':'noun',
        'eat':'noun',
        'book':'verb',
        'need':'verb',
        'want':'verb',
        'have':'verb',
        'hungry':'verb',
        'tired':'verb'
            }

        get_room =['room','rooms','bed','shower','beds','get','book','need','want','have','tired','sleep']
        go_bar =['food','drink','bar','table','eat','get','need','want','have','hungry']

        # Do you know which room you would like?
        room_yes_no= {
        'yes':'verb',
        'no':'verb',
        'do':'verb',
        'dont':'verb',
        "don't":'verb',
        'not':'verb',
        'know':'verb'
        }

        room_yes =['yes','do','know']
        room_no  =['no',"don't",'dont','not','know']

        # What room do you want?
        choose_room = {
        'small':'verb',
        'single':'verb',

        'medium':'verb',
        'double':'verb',


        'large':'verb',
        'king':'verb',
        'ensuite':'verb',

        'biggest':'verb',
        'queen':'verb',
        "queen's":'verb',
        'queens':'verb',
        'appartment':'verb',
        'room':'noun'
        }

        single_room =['small','single','room']
        double_room =['double', 'medium','room']
        large_room   =['large','king','en-suite','room']
        queen_room =['queen','biggest','apparment','furnished','queens','queen\'s','room']


        # Get more information from the gentlemen at the table
        get_more_information_with_intimidation ={
        'intimidation':"skill",
        'intimidate':"skill",
        'scare':"skill",
        }

        get_more_information_with_persuasion ={
        'persuasion':"skill",
        'persuade':"skill",
        'convince':"skill",
        'ask':"skill",
        'talk':"skill",
        }

        get_more_information_with_preception={
        'investigation':"skill",
        'investigate':"skill",
        'listen':"skill",
        'look':"skill",
        'find':"skill"
        }

        intimidation=['intimidation','intimidate','scare']
        persuasion=['persuasion','persuade','convince','ask','talk']
        preception=['investigation','investigate','listen','look','find']


        actions = {
        "fight":"action",
        "defuse":"action"
        }



        fight = ["fight"]
        defuse = ["defuse"]

numbers = {'one':1,
'two':2,
'three':3,
'four':4,
'five':5,
'six':6,
'seven':7,
'eight':8,
'nine':9,
'zero':0}
